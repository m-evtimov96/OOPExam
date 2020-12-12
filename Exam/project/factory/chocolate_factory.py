from project.factory.factory import Factory


class ChocolateFactory(Factory):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        types = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]

        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')
        if ingredient_type not in types:
            raise TypeError(f'Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}')

        if ingredient_type in self.ingredients:
            self.ingredients[ingredient_type] += quantity
        else:
            self.ingredients[ingredient_type] = quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients:
            if self.ingredients[ingredient_type] - quantity >= 0:
                self.ingredients[ingredient_type] -= quantity
            else:
                raise ValueError('Ingredient quantity cannot be less than zero')
        else:
            raise KeyError('No such product in the factory')

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name in self.recipes:
            if recipe_name in self.products:
                self.products[recipe_name] += 1
            else:
                self.products[recipe_name] = 1
            for ingr, quantity in self.recipes[recipe_name].items():
                self.ingredients[ingr] -= quantity
        else:
            raise TypeError('No such recipe')
