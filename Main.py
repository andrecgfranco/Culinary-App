from Recipe import Recipe
import Book
import Cook

recipe1 = Recipe("Pasta Carbonara", ["Spaghetti", "Bacon", "Eggs", "Parmesan", "Pepper"])
recipe2 = Recipe("Pasta Carbonara2", ["Spaghetti", "Guanchale", "Eggs", "Pecorinno", "Pepper"])
recipe3 = Book.to_recipe({"name": "Pasta Bolognese", "ingredients": ["Spaghetti", "Ground Beef", "Tomato", "Olive oil"]})

Book.save_recipe(recipe1)
Book.save_recipe(recipe2)
Book.save_recipe(recipe3)