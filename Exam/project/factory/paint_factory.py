from project.factory.factory import Factory


class PaintFactory(Factory):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        types = ["white", "yellow", "blue", "green", "red"]

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
            raise KeyError('No such ingredient in the factory')

    @property
    def products(self):
        return self.ingredients
