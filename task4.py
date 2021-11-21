class Car:
    color ="purple"
    type  = "Toyota Supra"
    year = 2019
    def __init__(self, color, type,year ):
        self.color = color
        self.type = type
        self.year = year

    def gelaunching(self):
        print("Автомобиль заведен")

    def getshutdown(self):
        print("Автомобиль заглушен")

    def setyeardate(self, year):
        self.year = year

    def settypeclass(self, type):
        self.type = type

    def setcolorstyle(self, color):
        self.color = color