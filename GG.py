class Organization:#Основний клас
    Cpu=0#Перемена
    HGz=0#Перемена
    Memory=0#Перемеа
    HDD=0#Перемена
    def __init__(self, Cpu, HGz, Memory,HDD):#конструктор
        self.Cpu = Cpu#Параметр
        self.HGz = HGz#Параметр
        self.Memory = Memory#Параметр
        self.HDD = HDD#Параметр

class Desktop(Organization):#другорядний клас(наслєдує основний)

    def __init__(self, Cpu, HGz, Memory,HDD,):#конструктор
        super().__init__(Cpu, HGz,Memory,HDD)#конструктор наслідує старі параметри
        self.Desktop=Desktop#Параметр
    def __repr__(self):#

        return "Desktop:" + "Cpu= " + str(self.Cpu) + " HGz= " + str(self.HGz) + " Memory= " + str(
            self.Memory) + " HDD= " + str(self.HDD)#вертає значення з функції
    def __str__(self):#представлення класу встороковому вигляді

        return  "Desktop:"+"Cpu= "+str(self.Cpu)+" HGz= "+str(self.HGz)+" Memory= "+str(self.Memory)+" HDD= "+str(self.HDD)#вертає значення з функції







class Laptop(Organization):# визивається для розробника


    def __init__(self, Cpu, HGz, Memory,HDD,):#визивається перед створенням обєктом класа
        super().__init__(Cpu, HGz,Memory,HDD,)#конструктор наслідує старі параметри
        self.Laptop = Laptop#Параметри

    def __repr__(self):# визивається для розробника

        return "Laptop:" + "Cpu= " + str(self.Cpu) + " HGz= " + str(self.HGz) + " Memory= " + str(
            self.Memory) + " HDD= " + str(self.HDD)#вертає значення з функції

    def __str__(self):# визивається для користувача
        return "Laptop:" + "Cpu= " + str(self.Cpu) + " HGz= " + str(self.HGz) + " Memory= " + str(self.Memory) + " HDD= " + str(self.HDD)#вертає значення з функції


class Server(Organization):# визивається для розробника

    def __init__(self, Cpu, HGz, Memory,HDD,):#визивається перед створенням обєктом класа
        super().__init__(Cpu, HGz,Memory,HDD,)#конструктор наслідує старі параметри
        self.Server = Server#Параметри


    def __str__(self):#
        return "Server:" + "Cpu= " + str(self.Cpu) + " HGz= " + str(self.HGz) + " Memory= " + str(
            self.Memory) + " HDD= " + str(self.HDD)#вертає значення з функції

    def __repr__(self):#представлення обєкту для розробника

        return "Server:" + "Cpu= " + str(self.Cpu) + " HGz= " + str(self.HGz) + " Memory= " + str(
            self.Memory) + " HDD= " + str(self.HDD)#вертає значення з функції




desktop=Desktop(4, 2.5, 6, 500)#створюєм зміну декстоп
print(desktop)#визивається магічгий метод який представляє клас встороковому вигляді


laptop=Laptop(2, 1.7, 4, 250)#створюєм перемєну лептоп
print(laptop)#визивається магічгий метод який представляє клас встороковому вигляді

server=Server(8, 3, 16, 2000)#створюєм перемєну сервер
print(server)#визивається магічгий метод який представляє клас встороковому вигляді


l=[#створення список
    [desktop,desktop, laptop,laptop, server],#содержымое списка
    [laptop,laptop,laptop],#параметри списка
    [desktop,desktop,desktop,laptop,laptop],#параметри списка
    [desktop,laptop,server,server]#параметри списка
]


for i in l:#цикл
    for g in i:#цикл
        print(g)#виводим(g)

sum=0#створюєм зміну для підрахуну кількості компютерів
for i in l:#цикл
    sum=len(i)+sum#додаєм довжину списка

print("Количиство компов= ",sum)#виводи (sum)

maxHDD=0#зміна в якій буде знаходитись макс.HDD

for i in l:#збиває великий списокна 4 малі

    for j in i:#розбиває список на содержымое

        if j.HDD>maxHDD:#якщо то
            maxHDD=j.HDD#присваюєм

print("max HDD=",maxHDD)#виводи (maxHDD)

minCPU=9999999999#створюєм перемєну
for i in l:#цикл
    for j in i:#цикл
        if j.Cpu<minCPU:#якщо то
            minCPU=j.Cpu#присваюєм
print("min CPU=",minCPU)#виводи (minCPU)


for i in l:#цикл
    for j in i:#цикл
        if type(j)==type(desktop):#якщо то
            j.Memory=8#присваюєм

