This is my first long term Python Project, while I'm learning Python this will serve as a test and practice for my skills.
It's in Portuguese for now and it consists in a program to store and use user-made recipes. 
# Recipes App

## Description

This is a Python project to store and use user-created recipes. The project serves as a long-term test and practice for Python skills. The app can generate shopping lists for saved recipes, suggest recipes based on a list of ingredients, and provide search functionalities for recipes by name and similar recipes.

## Features

- Store recipes
- Generate shopping lists
- Suggest recipes based on ingredients
- Search recipes by name
- Find similar recipes

## How to Use

1. **Store Recipes:**
   - Add new recipes by providing the name and ingredient list with: Livro.nova_receita() 

2. **Generate Shopping Lists:**
   - Get shopping lists for your saved recipes with: listaDasCompras(recipe_name)

3. **Recipe Suggestions:**
   - Receive recipe suggestions based on available ingredients with: sugere(ingredients) or sugere(nova_lista())
   - nova_lista() creates a list of strings that are taken as ingredients, by asking for input one by one and finishing if the input is empty

4. **Search by Name:**
   - Search for specific recipes using their names with: search_receita(recipe_name)

5. **Find Similar Recipes:**
   - Discover recipes similar to a given one with: search_similar(recipe)
