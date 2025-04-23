function getRecommendations() {
    let budget = document.getElementById("budget").value;
    let category = document.getElementById("category").value;
    let resultsDiv = document.getElementById("results");

    if (!budget || !category) {
        resultsDiv.innerHTML = `<p style="color:red;">Please enter a budget and select a category!</p>`;
        return;
    }

    fetch(`/recommend?budget=${budget}&category=${category}`)
        .then(response => response.json())
        .then(data => {
            resultsDiv.innerHTML = "";
            if (data.error) {
                resultsDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
                return;
            }

            data.recommendations.forEach(res => {
                let card = document.createElement("div");
                card.className = "restaurant-card";
                card.innerHTML = `
                    <h3>${res.Restaurant_Name}</h3>
                    <p><b>Category:</b> ${res.Category}</p>
                    <p><b>Pricing for 2:</b> ₹${res.Pricing_for_2}</p>
                    <p><b>Dining Rating:</b> ⭐${res.Dining_Rating}</p>
                    <p><b>Delivery Rating:</b> ⭐${res.Delivery_Rating}</p>
                    <p><b>Location:</b> ${res.Locality}</p>
                `;
                resultsDiv.appendChild(card);
            });
        })
        .catch(error => {
            console.error("Error:", error);
            resultsDiv.innerHTML = `<p style="color:red;">Something went wrong. Please try again.</p>`;
        });
}
