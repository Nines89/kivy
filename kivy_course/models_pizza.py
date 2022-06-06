

class Pizza:
    name = ""
    ingredients = ""
    price = 0.0
    vegetarian = False

    def __init__(self, name, ingredients, price, vegetarian):
        self.name = name
        self.ingredients = ingredients
        self.vegetarian = vegetarian
        self.price = price

    def get_pizza_dict(self):
        return {"name": self.name, "ingredients": self.ingredients,
                "price": str(self.price), "vegetarian": self.vegetarian}