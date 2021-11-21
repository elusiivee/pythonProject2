class Country:
    name = ""

class Russia(Country):
    population=20000000
    def __init__(self,name,peolpe):
        self.name = name
        self.population=peolpe
    def setPopulation(self,people):
        self.population=people
    def getPopulation(self):
        print(self.population)

class Canada(Country):#наследования
    __population = 2

    def __init__(self, name, peolpe):
        self.name = name
        self.population = peolpe

    def setPopulation(self, people):
        self.population = people

    def getPopulation(self):
        print(self.population)

a=Canada("Canada",3)
b=Russia("Russia",1)
a.setPopulation(70)
print("Country", a.name , "with population", a.population)