from Recipe import Recipe
import Book
import json

def shopping_list(str):
    with open("Book_Of_Recipes.json", "r") as file:
        for line in file:
            x = json.loads(line)
            if x["name"] == str:
                print("=" * 30)
                print("buy: \n")
                for n in x["ingredients"]:
                        print(f"- {n}")
                print("=" * 30)
                break

def suggest(ingredients):
    suggest = []
    for r in Book.list_recipes():
        if all(ing in ingredients for ing in r.get_ingredients()):
            suggest.append(r)
    if not suggest: 
        print("I've got no suggestions for these ingredients")
    else:
        print("I suggest:")
        for s in suggest:
            s.show_recipe()
