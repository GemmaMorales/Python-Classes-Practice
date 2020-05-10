# 1. Objects are defined as classes first, using the "Class" statement
class Car:

    def __init__(self): 
        self.make = None
        self.used = None
        self.brand = None
        self.velocity = 0
        self.on = False
        self.horse_power = 10
        self.steering_position = 0
        print("New car has been created with velocity" +str(self.velocity))

    # feet_force: from 1 - 100 how hard is the foot pressing
    def accelerate(self, feet_force):
        print(f"Accelerating... percentage {str(feet_force)}%")
        self.velocity = self.velocity + (self.horse_power / feet_force)
        print("New velocity is: " +str(self.velocity))



car1 = Car()
car1.brand = "Toyota"
car1.make = "V12ABF456"
car1.horse_power = 20
car1.accelerate(80)

car2 = Car()
car2.brand = "Ford"
car2.make = "23FVBG56"
car2.horse_power = 550
car2.accelerate(80)
