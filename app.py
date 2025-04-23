from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
knn_model = joblib.load("restaurant_knn_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load dataset
file_path = "cleaned_restaurants.csv"
df = pd.read_csv(file_path)

# Select relevant features
features = ['Pricing_for_2', 'Dining_Rating', 'Delivery_Rating']

# Normalize data using the same scaler from training
df_scaled = scaler.transform(df[features])

# Function to get restaurant recommendations based on budget and category
def recommend_restaurant_by_budget(budget, category, n_recommendations=5):
    # Filter dataset based on budget
    filtered_df = df[df['Pricing_for_2'] <= budget]
    filtered_df = filtered_df[filtered_df['Category'].str.contains(category, case=False, na=False)]

    if filtered_df.empty:
        return {"error": "No restaurants found within this budget and category."}

    # Get scaled features for the filtered restaurants
    filtered_indices = filtered_df.index.tolist()
    filtered_scaled = df_scaled[filtered_indices]

    # Find nearest neighbors using KNN model
    distances, indices = knn_model.kneighbors(filtered_scaled, n_neighbors=n_recommendations)

    # Get recommended restaurant indices
    recommended_indices = np.unique(indices.flatten())[:n_recommendations]

    # Get restaurant details
    recommendations = df.iloc[recommended_indices]
    
    return recommendations[['Restaurant_Name', 'Category', 'Pricing_for_2', 'Dining_Rating', 'Delivery_Rating', 'Locality']].to_dict(orient="records")

# Route for the UI
@app.route('/')
def index():
    categories = sorted(df['Category'].unique())  # Get unique categories for dropdown
    return render_template('index.html', categories=categories)

# API Route to get recommendations
@app.route('/recommend', methods=['GET'])
def recommend():
    budget = request.args.get('budget', type=int)
    category = request.args.get('category', type=str)
    
    if not budget or not category:
        return jsonify({"error": "Please provide both budget and category!"}), 400

    recommendations = recommend_restaurant_by_budget(budget, category)
    
    return jsonify({"budget": budget, "category": category, "recommendations": recommendations})

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
