class Recipe:
    def __init__(self, name, list_ingredients):
        self.name = name
        self.list_ingredients = list_ingredients
    
    def get_name(self): 
        return self.name

    def get_ingredients(self):
        return self.list_ingredients

    def show_ingredients(self):
        separator = ", "
        result_string = separator.join(self.list_ingredients)
        return ("["+ result_string +"]")
            
    def show_recipe(self):
        print("=" * 30)
        print(f"Recipe: {self.name} \n Ingredients:")
        for n in self.list_ingredients:
            print(f"- {n}") 
        print("=" * 30)

