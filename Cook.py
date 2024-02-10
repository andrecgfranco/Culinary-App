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
    ingredients_lower = [ing.lower() for ing in ingredients]
    for r in Book.list_recipes():
        r_lower = [ing.lower() for ing in r.get_ingredients()]
        if all(ing in ingredients_lower for ing in r_lower):
            suggest.append(r)
    if not suggest: 
        print("I've got no suggestions for these ingredients")
    else:
        print("I suggest:")
        for s in suggest:
            s.show_recipe()
