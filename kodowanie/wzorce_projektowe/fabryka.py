# Wzorzec fabryka polega na definiowaniu interfejsu do tworzenia obiektu, ale pozwala klasom podrzędnym na zmianę typu tworzonych obiektów.
# Jest szczególnie użyteczny, gdy istnieje wiele klas pochodnych i chcemy ukryć logikę ich tworzenia przed klientem.


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    pets = dict(dog=Dog(), cat=Cat())
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
