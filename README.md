# 🍽️ Restaurant Recommendation System

This project is a simple Flask web application that recommends restaurants based on user preferences like budget and food category. It uses a K-Nearest Neighbors (KNN) model trained on a dataset of restaurants.

---

## 🚀 Features

- Input your **budget** and **food category** to get personalized restaurant recommendations.
- Uses a pre-trained **KNN model** and **MinMaxScaler** for feature normalization.
- Powered by **Flask** and served via **Gunicorn** for production environments.

---

## 🧠 Tech Stack

- **Backend Framework**: Flask
- **Modeling**: scikit-learn, joblib
- **Data Manipulation**: pandas, numpy
- **Web Server**: Gunicorn (for deployment)

---

## 📁 Project Structure

```
Restaurant-Recommendation-System/
│
├── app.py                      # Main Flask app
├── cleaned_restaurants.csv     # Dataset used for recommendations
├── restaurant_knn_model.pkl    # Trained KNN model
├── scaler.pkl                  # Trained scaler for normalization
├── requirements.txt            # Python dependencies
├── Procfile                    # Gunicorn process file for deployment
└── README.md                   # This file
```

---

## ⚙️ Installation

1. Clone the repository or download the ZIP.

```bash
git clone <repo_url>
cd Restaurant-Recommendation-System
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Run the application locally.

```bash
python app.py
```

The app will start running at `http://127.0.0.1:5000/`

---

## ☁️ Deployment (Heroku Example)

1. Create a Heroku app:

```bash
heroku create restaurant-recommender
```

2. Push the code:

```bash
git push heroku main
```

3. Open the app:

```bash
heroku open
```

> Make sure your `Procfile` and `requirements.txt` are present in the root directory.

---

## 📝 Inputs & Output

**Inputs**:
- Budget (numerical)
- Food category (e.g., "Chinese", "Italian")

**Output**:
- JSON or HTML view of top recommended restaurants

---

## 🛠 Future Enhancements

- Add user authentication
- Use collaborative filtering
- Include location-based filtering using geolocation
- Build a frontend with React or Vue.js

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
