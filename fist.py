#1
'''def arithmetic(num1, num2, op):
    if op == '-':
        return num1 - num2 # повертає результат виконання функції в пам*ять
    elif op == '*':
        return num1*num2
    elif op == '+':
        return num1+num2
    elif op == '/':
        return num1/num2

a,b,c = int(input("Input a")), int(input("Input b")), input("Input operation")
x = arithmetic(a,b,c) # 1 варіант : змінна х фактично зберігає результат виконання функції (зберігаємо в змінній)
print("The result of op:", x)

print(arithmetic(a, b, c)) # або просто роздрукувати на екран

""" Інтерактивність """
# print("Input num1, num2, operation!")
# num1=int(input())
# num2=int(input())
# operation=input()


num1,num2,operation = int(input("Input 1st_num")), int(input("Input 2nd_num")), input("Input operation")

def arithmetic(num1,num2,operation):
    if operation == "+":
        print(num1+num2)
    if operation == "-":
        print(num1 - num2)
    if operation == "*":
        print(num1*num2)
    if operation == "/":
        print(num1/num2)

arithmetic(num1, num2, operation) # коли функція нічого не повертає, її просто викликають

year=int(input()
def is_year_leap(year)
!!!'''
import math
import string

'''Написать функцию square, принимающую 1 аргумент — сторону квадрата,
 и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
import math


def square(side):
    square=side*side
    p=(side+side)*2
    d=2*(math.sqrt(2))
    return square,p,d


x=square(6)
print(x)
 
 '''

'''Написать функцию season,
 принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит 
 (зима, весна, лето или осень).
 s1 = "HelloAAA"
print(s1[-1::-1]) # AAAolleH

my_list = ['asf', True, 'asf', 15.5, 245]
print(my_list[1], my_list[-4])
x = my_list[0:3]
print(x)

months = (1, 2, 3, 4, 5)
print("The 1st element",months[0]) # c
print(months) # [звідки(включно):куди(невключно):крок]
#print(months[0:])
print(months[-1:0:-1])

 '''




'''

1)Їбашити по 2 часа в день -            
2) Оприділитись по направлені в пітоні(ютуб фраймворкі пітон)-
3) пройтивсе до строк в степікж-
4) конспект за 2 дня до уроку+
5) продумати проект(особистий), подивитись як писати тз(технічне)?
6) навести порядок+
'''



'''2.5 геометрическая прогресия ???????????????


b=int(input())
q=int(input())
n=int(input())
print(b-q**(n-1))'''

'''
satimetr=int(input())
print(satimetr//100)
'''

'''
n=int(input())
k=int(input())
dost=k//n
ost=k%n
print(dost)
print(ost)

'''
'''????????????????????????????????????
list=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)
a=input()
if a=list[-34:-29:1]:
    print(1)
print(list[-34:-30:1])

'''


'''time=int(input())
hour=time//60
minutes=time%60
print(hour)
print(minutes)
print(time, "мин", "-", "это", hour, "час", minutes, "минут.")'''




'''num=int(input())
d=num%10
c=num%100//10
b=(num%1000)//100
a=(num%10000)//1000
print("Цифра в позиции тысяч равна",a)
print("Цифра в позиции сотен равна",b)
print("Цифра в позиции десятков равна",c)
print("Цифра в позиции единиц равна",d)'''




'''point=int(input())
if point>-30 and point <=-2:
    print("Принадлежит")
elif point>7 and point<=25:
    print("Принадлежит")
else:
    print("Не принадлежит")'''

'''a=int(input())
b=int(input())
c=int(input())

if a+b>c and a+c>b and b+c>a:
    print("YES")
else:
    print("NO")'''


'''a=int(input())
if a%2==0:
    print("31")
elif a ==2:
    print("28")
elif a/2!=0:
    print("30")'''


'''weight=int(input())
if weight<60:
    print("Легкий вес")
elif weight >=60 and weight<64:
    print("Первый полусредний вес")
elif weight >=64 and weight <69:
    print("Полусредний вес")'''



'''first=int(input())
second=int(input())
sign=input()
if sign =="+":
    print(first + second)
elif sign =="-":
    print(first - second)
elif sign =="*":
    print(first * second)
elif sign =="/":
    if second !=0:
        print(first / second)
    elif second ==0:
        print("На ноль делить нельзя!")'''


'''for i in 'hello world':
     if i == 'a':
        break
else:
    print('Буквы a в строке нет')'''






'''написати функцію яка приймає першим аргументом список, другим аргументом приймає функція наш вибір, '''





'''def get_value():
    return input("Введіть будь ласка значення!")


def get_index():
    return int(input("Введіть будь ласка індекс!"))


def show_list():
    print("Ваш список виглядає")


def work_with_list(l, choice):
    ''''''l=list()
    if choice==1:
        print("Зараз спрацює метод append")
        value =input("Введіть змінну яку хочете ввести")
        l.append(value)
        show_list()
        return (l)

    elif choice==2:
        l2 = [1, 2, 4, 5]
        print("Зараз спрацює метод extend")
        l.extend(l2)
        show_list()
        return (l)

    elif choice==3:
        print("Зараз спрацює метод insert")
        # index = get_index()
        # value = get_value()
        # l.extend(index, value)
        l.extend(get_index(), get_value())
        show_list()
        return (l)

    elif choice == 4:
        print("Зараз спрацює метод remove")
        l.remove(get_value())
        show_list()
        return (l)

    elif choice == 5:
        print("Зараз спрацює метод pop")
        x=l.pop(get_index())

        return(x)

    elif choice == 6:
        value = input("Введіть змінну яку хочете підщитати")
        x=l.count(value)
        print("Кількість елементів такого значення:")
        return(x)

    elif choice == 7:
        print("Зараз спрацює метод sort")
        print("Список до сортіровки",l)
        l.sort()
        print("список після сортіровки")
        return(l)

    elif choice == 8:
        print("Зараз спрацює метод reverse")
        l.reverse()
        show_list()
        return (l)

    elif choice==9:
        print("Зараз спрацює метод copy")
        x=l.copy()
        show_list()
        return (x)

    elif choice==10:
        print("Зараз спрацює метод clear")
        x=l.clear()
        return (x)

    elif choice==11:
        print("Зараз підщитаєм суму всіх елементів")
        return sum(l)
    elif choice==12:
        print("Зараз підщитаєм довжину списку")
        return len(l)
    elif choice==13:
        print("Зараз найдем найменше значення списку")
        return min(l)
    elif choice==14:
        print("Зараз найдем найбільше значення списку")
        return max(l)
    elif choice==15:
        print("Зараз найдем номер строки")
        return(lZ.find(mylist))

mylist=["car","book",2,"dance",8]


choice = int(input("Введіть номер від 1-13"))
res=work_with_list(mylist,choice)
print(res)

while choice!=10:#програма зворачується якщо список буде очищений
        choice = int(input("Введіть номер від 1-13"))
        res = work_with_list(mylist, choice)
        print(res)'''




'''написаи функцю для строк(замість цифр- текст)'''

'''
степік пройти до списків+ написати функцію таку саму для строк як і робили(інтерактивно)
Відос по функціям + конспект найти актуальні методи для сток 
скачати anydesk
'''





'''def work_with_list(a, choice, width, start, finish):

    if choice==1:
        print("Зараз спрацює метод len")
        return len(a)

    elif choice==2:
        print("Зараз спрацює метод isdigit")#?
        return(a.isdigit())
    elif choice==3:
        print("Зараз спрацює метод isalpha")#?
        return(a.isalpha())
    elif choice==4:
        print("Зараз спрацює метод islower")
        return(a.islower())
    elif choice==5:
        print("Зараз спрацює метод isupper")#?
        return(a.isupper())
    elif choice==6:
        print("Зараз спрацює метод isspace")#?
        return(a.isspace())
    elif choice==7:
        print("Зараз спрацює метод upper")
        return(print(a.upper()))
    elif choice==8:
        print("Зараз спрацює метод lower")
        return(print(a.lower()))
    elif choice==9:
        print("Зараз спрацює метод capitalize")
        return(print(a.capitalize()))
    elif choice==10:
        print("Зараз спрацює метод title")
        return(print(a.title()))
    elif choice==11:
        print("Зараз спрацює метод zfill")#?
        return(print(a.zfill(width)))
    elif choice==9:
        print("Зараз спрацює метод capitalize")
        return(print(a.capitalize()))
    elif choice==9:
        print("Зараз спрацює метод capitalize")
        return(print(a.capitalize()))
    elif choice==9:
        print("Зараз спрацює метод capitalize")
        return(print(a.capitalize()))




def menu():
    choice=int(input("Введіть номер від 1-13"))
    return choice


a="plate car photo Rocket plane 123"

choice=menu()
res=work_with_list(a,choice,10,7,9)
print(res)'''




'''
def get_keys():

    keys = ['name', 'surname', 'age', 'birthday', 'job', 'country', 'city', 'sport',
            'budget', 'like to eat', 'like to drink', 'pat', 'phone number', 'car(yes/no)',
            'plane(yes/no)']
    return keys


def get_Value():

    values = [input("name:"), input("surname:"), int(input("age")), int(input("birthday:")), input("job:"), input("country:"),
              input("city:"), input("sport:"), int(input("budget:")), input("like to eat:"), input("like to drink:"), input("pat:"),
              int(input("phone number:")), input("car(yes/no):"), input("plane(yes/no):")]
    return values





info = dict(zip(get_keys(), get_Value()))
for key in info:
        print(key, ":", info[key]) # info[key] , key
'''


# dic={1:"Jan", 2:"Fed", 3:"Mar",4:"Apr",5:"Jun",6:"Jul"}
#
# def open_Dic(dic):
#     for i in range(1,len(dic)):
#         print(dic[i])
#     return dic
# open_dik=open_Dic(dic)
# print(open_dik)


# def add_twonums(a:float,b:float)->float: #ZeroDivision
#     '''
#     The function sums two arguments
#     :param a: the first float number
#     :param b: the second float number
#     :return: sum
#     '''
#     if b==0:
#         raise ZeroDivisionError("☺")
#     if (isinstance(a, float) and isinstance(b, float)) \
#             or (isinstance(a, int) and isinstance(b, int)):
#         return a/b
#     else:
#         raise TypeError("One of two nums is incorrect")
#
# print(add_twonums(5,0))







# def sort_The(numbers:list):
#     '''
#     the function must convert each elements in type(int), sort them and revers and print them on the scrin
#     :param numbers:
#     :return:
#     '''
#
#     l=[]
#
#     for i in range(len(numbers)):
#         try:
#             a = int(numbers[i])
#         except:
#             raise TypeError("ERORRRR♥")
#
#         l.append(a)
#
#     l.sort()
#     print(*l)
#     l.sort(reverse=True)
#     print(*l)
#
#
#
#
#
# def get_List_Of_string():
#     x=input("Input list").split()
#     return x
#
#
# a=get_List_Of_string()
# sort_The(a)
# numbers = int(input())
# l=[]
# for i in range(numbers):
#     l.extend(input())
# print(l)





# def longest_set(a:set,b:set)->set:
#     '''
#     The function is sexy
#     :param a:
#     :param b:
#     :return:
#     '''
#     return a if len(a)>len(b) else b
#
# print(longest_set(,)
'''прийняти список кортеж аьо тапл потім провіряю чи я це прийняв і вертаю множину'''

# def cool_set(a:any,b:any)->tuple:
#     '''
#
#     :param a:
#     :param b:
#     :return:
#     '''
#     if not isinstance(a,(dict,tuple,list,str)) and\
#             isinstance(b,(dict,tuple,list,str)):
#         raise ValueError("a or b is not dict,tuple,list,str")
#     return set(a),set(b)
#
# print(cool_set("fdhdf", "123456"))
# print(cool_set(12345,"dfgjk"))



# a=[1,2,4]
# numbers = [a for i in range(10)]
# print(numbers)
#
'''реалізуваи функцію що приimport random
# #
# # kub=[random.randint(1,10) for i in range(101)]
# # strok=[random.random()]
# # print(kub)
# 
# # def rand_words():
# #
# #     strok = [(1,3,6) for i in range(10)]
# #     print(strok)
# #
# # rand_words()
# 
# 
# def get_A_B_C():
#     return int(input('Введіть a')),int(input('Введіть b')),int(input("Введіть кількість ітерації"))
# 
# 
# 
# 
# def random_list(a:int,b:int,c:int)->list:
#     '''
#
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     '''
#     return {random.randint(a, b) for i in range(c)}
#
#
# a,b,c=get_A_B_C()
# z=random_list(a,b,c)
# from random import randint
#
# num=randint(1, 3)
# my=input("ваш знак:")
# sign=""
# if num ==1:
#     sign = "ножниці"
#     print(sign)
# elif num ==2:
#     sign = "камень"
#     print(sign)
# elif num ==3:
#     sign = "бумага"
#     print(sign)
#
#
# if my == "ножниці":
#     if sign == "бумага":
#         print("ви виграли")
#     elif sign == "камень":
#         print("ви програли")
#     elif sign == "ножниці":
#         print("нічия")
# elif my == "бумага":
#     if sign == "камінь":
#         print("ви виграли")
#     elif sign == "ножниці":
#         print("ви програли")
#     elif sign == "бумага":
#         print("нічия")
# elif my == "камінь":
#     if sign == "ножниці":
#         print("ви виграли")
#     elif sign == "бувага":
#         print("ви програли")

def find_all(target, symbol):
    l=[]
    for i in range(len(target)):
        if target[i]==symbol:
            l.append(i)

    return l


x=find_all(target=input(), symbol=input())
print(x)
╨