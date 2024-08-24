# create a class
class Bike:
    name = ""
    gear = 0

# create objects of class
bike1 = Bike()    

bike1.gear = 11
bike1.name = "Mountain bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")


class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of room: ", self.length * self.breadth)

study_room = Room()
study_room.breadth = 75
study_room.length = 100
 
study_room.calculate_area()
