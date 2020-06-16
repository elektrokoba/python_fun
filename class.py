class Car:

    def __init__(self, level, doors):
        self.__fuelLevel = level
        self.__numberOfDoors = doors
        print("Constructing object with params: ", str(level) , str(doors))
    
    def fillTank(self):
        self.__fuelLevel = 100
        print("This is a message inside the class.")

    def getFuelLevel(self):
        return self.__fuelLevel

    def setFuelLevel(self, fuelLevel):
        self.__fuelLevel = fuelLevel

bmw = Car(10, 4)
vw = Car(23, 5)

bmw.setFuelLevel(53)
bmw.fillTank()
print(bmw.getFuelLevel())
