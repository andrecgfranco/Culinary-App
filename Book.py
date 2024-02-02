from Recipe import Recipe
import json
import os

#Cria uma Recipe com base num dicionario
def to_recipe(dic):
    return Recipe(dic["name"],dic["ingredients"])

#Retorna a list de todas as Recipes
def list_recipes():
    file_path = "Book_Of_recipes.json"  
    recipes = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                recipe_data = json.loads(line.strip())  
                recipes.append(to_recipe(recipe_data))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return recipes

#Mostra todas as Recipes no Livro
def show_recipes():
    if not list_recipes():
        print("There are no recipes") 
    for r in list_recipes():
        r.show_recipe()

#Guarda uma Recipe no Livro
def save_recipe(r):
    with open("Book_Of_recipes.json", 'a') as file:
        l = list_recipes()
        if not is_saved(r):
            recipe_data = {
                'name': r.get_name(),
                'ingredients': r.get_ingredients()
            }
            file.write(json.dumps(recipe_data) + "\n")
            print(f"Recipe {r.get_name()} Saved")
        else:
            print(f"Recipe {r.get_name()} was already saved")

#Verifica se uma Recipe ja esta guardada 
def is_saved(r):
    name = r.get_name()
    with open("Book_Of_recipes.json", 'r') as file:
        for line in file:  
            x = json.loads(line)
            if x['name'] == name:
                return True
        return False

#Apaga todas as Recipes
def wipe_book():
    os.remove("Book_Of_recipes.json")

#Remove Recipes pelo name
def remove_recipe(name):
        with open("Book_Of_recipes.json", 'r') as file:
            lines = file.readlines()

        with open("Book_Of_recipes.json", 'w') as file:
            for line in lines:
                line1 = json.loads(line)
                if line1["name"] != name: 
                    file.write(line)

        print(f"{name} was removed from the Book")

#Pesquisa de Recipes pelo name
def search_recipe(name): 
    found = False
    with open("Book_Of_recipes.json", 'r') as file:
        for line in file:
            dict = json.loads(line)
            if name == dict["name"]:
                Recipe.show_recipe(to_recipe(dict))
                found = True
    if not found:
        print("Could not find the recipe")

#Procura Recipes parecidas (3 ou mais ingredients em comum)
def search_similar(r):
    list_recipes = []
    with open("Book_Of_recipes.json", 'r') as file:
        for line in file:
            recipe = to_recipe(json.loads(line))
            if (in_common(recipe, r) >= 3 and recipe.get_name() != r.get_name()):
                list_recipes.append(recipe)
    if list_recipes:
        if (len(list_recipes) == 1):
            print("Here's a similar recipe:")
            list_recipes[0].show_recipe()
        else:
            print("Here are some similar recipes:")
            for recipe in list_recipes:
                recipe.show_recipe()
    else:
        print("Couldn't find similar enough recipes")

#Verifica quantos ingredients em comum entre duas Recipes
def in_common(r1, r2):
    i1 = r1.get_ingredients()
    i2 = r2.get_ingredients()
    n = 0
    for ing in i1:
        if ing in i2:
            n += 1
    return n

#Cria uma list de ingredients por input do user
def new_list():
    ret = []
    while True:
        x = input("Add an ingredient (leave blank if finished) \n")
        if x != "":
            ret.append(x)
        else: 
            break
    return ret

#Cria e guarda uma new Recipe atraves de input do user
def new_recipe():
    name = input("What's the recipe's name? \n")
    ingredients = new_list()
    r = Recipe(name, ingredients)
    r.show_recipe()
    save_recipe(r)