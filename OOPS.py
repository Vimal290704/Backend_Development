class Person:
    pass  # it helps you save from empty classes

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person(input("Enter your name: "), int(input("Enter your age: ")))
print(p1.name, p1.age)


class Vehicle:
    name = "Lambo"
    model = "78URS7"


class Car(Vehicle):
    pass


cr = Car()
print(cr.name + cr.model)
