class Animal:
    def talk(self):
        print(f'{self.sound}')

class Dog(Animal):
    def __init__(self, sound):
        self.sound = sound

class Cat(Animal):
    def __init__(self, sound):
        self.sound = sound

Grushka = Cat('meow')
Greta = Dog('woof')

def make_sound(animal):
    if isinstance(animal, (Cat, Dog)):
        return animal.talk()
    else:
        return "Invalid input"

make_sound(Grushka)
