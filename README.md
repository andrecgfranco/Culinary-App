This is my first long term Python Project, while I'm learning Python this will serve as a test and practice for my skills.
It consists in a program to store and use user-made recipes. 
# Recipes App

## Description

This is a Python project to store and use user-created recipes. The project serves as a long-term test and practice for Python skills. The app can generate shopping lists for saved recipes, suggest recipes based on a list of ingredients, and provide search functionalities for recipes by name and similar recipes.

There is no UI yet, but it's on it's way

## Features

- Store recipes
- Generate shopping lists
- Suggest recipes based on ingredients
- Search recipes by name
- Find similar recipes

## How to Use

1. **Store Recipes:**
   - Add new recipes to a JSON file by providing the name and ingredient list with: Book.new_recipe(). This will, if it's the first time, create a file that represents your recipe book (Livro_De_Receitas.json) and save the recipe there, otherwise it'll append the new recipe to the file

2. **See Recipes:**
   - See a recipe with: Recipe.show_recipe()
   - See all the saved recipes with: list_recipes()

2. **Generate Shopping Lists:**
   - Get shopping lists for your saved recipes with: shopping_list(recipe_name)

3. **Recipe Suggestions:**
   - Receive recipe suggestions based on available ingredients with: suggest(ingredients) or suggest(new_list())
   - new_list() creates a list of strings that are taken as ingredients, by asking for input one by one and finishing if the input is empty

4. **Search by Name:**
   - Search for specific recipes using their names with: search_recipe(recipe_name)

5. **Find Similar Recipes:**
   - Discover recipes similar to a given one with: search_similar(recipe)
