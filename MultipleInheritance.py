print("***************************************************************************************************************")

print("Write a code to perform multiple inheritance.")

class Engine:
    def start_engine(self):
        print("Engine is getting started!")

    def stop_engine(self):
        print("Engine has stopped!")

class Wheels:
    def move(self):
        print("Wheels have started moving!")

    def brake(self):
        print("Brakes applied!")

class Car(Engine, Wheels):
    def honk(self):
        print("Car horn!!")

car = Car()

car.start_engine()
car.move()
car.honk()
car.brake()
car.stop_engine()

print("***************************************************************************************************************")
