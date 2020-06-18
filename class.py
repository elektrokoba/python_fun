class Car:

    def __init__(self, level, doors, color, cartype):
        self.__fuelLevel = level
        self.__numberOfDoors = doors
        self.color = color
        self.type = cartype
        print("Constructing object with params: ", str(level) , str(doors), str(color), str(cartype))
    
    def fillTank(self):
        self.__fuelLevel = 100
        print("This is a message inside the class.")

    def getFuelLevel(self):
        return self.__fuelLevel

    def setFuelLevel(self, fuelLevel):
        self.__fuelLevel = fuelLevel
    
    def getColor(self):
        return self.color

    # ez azert hibas, mert a get elvarja a color-t, tehat nem kell atadni a color parametert 
    # def getColor(self, color):
    #     return self.color

# Eddig a vonalig van a class definíciója
# ---------------------------------------

#  ha nem definialom a color-t és a cartype-t az hiba
# vw = Car(23, 5)
bmw = Car(12, 4, "blue", "hatchback")


bmw.setFuelLevel(53)
bmw.fillTank()
print("bmw.getFuelLevel: ", bmw.getFuelLevel())
print("bmw.getColor: ", bmw.getColor())
print("bmw.color", bmw.color)

# print("vw.getFuelLevel: ", vw.getFuelLevel())
#  ha nem definialom a color-t akkor nem is tudom lekérdezni
# print("vw.getColor: ", vw.getColor())
# print("vw.color", vw.color)


#TODO private protected, public dolgok ezen kiprobalni
