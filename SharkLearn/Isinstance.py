class Fruit:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('INVALID FRUIT')

    def __str__(self):
        return self.__class__.__name__


class Banana(Fruit):
    def __init__(self):
        super().__init__('Banana')

    def eat(self):
        print('Banana must be peeled then eaten.')


class Apple(Fruit):
    def __init__(self):
        super().__init__('Apple')

    def eat(self):
        print('Apple can be eaten.')


class Strawberry(Fruit):
    def __init__(self):
        super().__init__('Strawberry')

    def eat(self):
        print('Apple can be eaten.')


fruits = [Banana(), Apple(), Strawberry()]

for fruit in fruits:
    fruit.eat()
