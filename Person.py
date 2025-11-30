print("***************************************************************************************************************")

print("Define a class Person with attributes name and age. Create an instance of this class and print its attributes.")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Kiran", 28)

print("Name :: ", person.name)
print("Age :: ", person.age)

print("***************************************************************************************************************")
