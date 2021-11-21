class Games:
    yaer=0
    name="brawlstars"



    def __init__(self,year,name):
        self.year = year
        self.name = name

    def setYearNumber(self, year):
        self.year = year
    def setName(self,name):
        self.name=name


class PCGames(Games):
    agerestriction=18
    budget=100000
    def __init__(self, year, name, age, budget):
        super().__init__(year, name)
        self.agerestriction=age
        self.budget=budget
    def getINfo(self):
        print("Гра",self.name,"\n", "створена в", self.year, "\n", "Вікове обмежння", self.agerestriction,"\n", "Бюджет", self.budget,"карбованців")

a=PCGames(2019, "CS-GO", 18, 100)
a.getINfo()