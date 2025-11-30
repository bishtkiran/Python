print("***************************************************************************************************************")

print("Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.")

class Animal:
    def sound(self):
        print("Zzzzzz!!!")

class Dog(Animal):
    def sound(self):
        print("Bark!!")

class Cat(Animal):
    def sound(self):
        print("Meow!!")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

print("***************************************************************************************************************")
