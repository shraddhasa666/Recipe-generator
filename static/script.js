document.getElementById("searchBtn").addEventListener("click", function() {
  const ingredients = document.getElementById("ingredientInput").value;
  fetch(`/search?ingredients=${encodeURIComponent(ingredients)}`)
    .then(response => response.json())
    .then(data => {
      const resultsList = document.getElementById("resultsList");
      resultsList.innerHTML = "";

      if (!data || data.length === 0) {
        resultsList.innerHTML = '<p class="text-center">No recipes found.</p>';
        return;
      }

      data.forEach(recipe => {
        const cardDiv = document.createElement("div");
        cardDiv.className = "col-md-6 mb-3";

        cardDiv.innerHTML = `
          <div class="card h-100">
            <img src="${recipe.image}" alt="${recipe.name}" class="card-img-top">
            <div class="card-body">
              <h5 class="card-title">${recipe.name}</h5>
              <p><strong>Ingredients:</strong> ${recipe.ingredients.join(", ")}</p>
              <p><strong>Prep Time:</strong> ${recipe.prep_time} | <strong>Cook Time:</strong> ${recipe.cook_time}</p>
              <p><strong>Nutrition:</strong> ${recipe.nutrition}</p>
              <p><strong>Recipe:</strong> ${recipe.recipe}</p>
            </div>
          </div>
        `;

        resultsList.appendChild(cardDiv);
      });
    });
});
