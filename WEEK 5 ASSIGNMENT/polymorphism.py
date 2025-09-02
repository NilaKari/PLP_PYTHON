# ==============================
# Activity 2: Polymorphism Challenge
# ==============================

# Base class: Vehicle
class Vehicle:
    def move(self):
        print("This vehicle moves somehow...")

# Subclasses with polymorphic move()
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")


# Example usage of polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()

# Output:
# Driving 🚗
# Flying ✈️
# Sailing ⛵