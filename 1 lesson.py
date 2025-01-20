# int (interger) целые числа
a = 5
b = 6
name = "Sasha"
f = 24

print (a)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%2) # остаток от деления

NAME = "const" # договорились контстанты именовать заглавными буквами

print("Sasha") # или:
print('Sasha')

# Форматированные строки
print(f'Hello/ a+b={a+b}')

"""
Комментарии многострочные
"""

'''
Комментарии многострочные
'''
# float действительные числа
c= 5.7
d= 7.0

print(type(a))
print(type(c))
print(type(a+c))


# тип данных bool
print(7 < 10)
print(7 > 10)
print(7 <= 10)
print(7 >= 10)
print(7 == 10)
print(7 != 10)

# string
age = 24 # пока это строка
print(int(age) + 1) # int преобразуем age в число
last_name = (
    "Ivanov"
    "Ivanov"
)

text = """
hjlhldgf
gdjgd;g
"""

city = "Moscow\ncity" # \n конец строки
print(last_name)

# списки. Для хранения нескольких данных в одной переменной (массив)
numbers = []
new_number = [1,2,3]
elements = [1,2,'name']
print(elements)

cars = list() # альтернативный способ создания списка (дольше обрабатывается машиной)

# кортеж - неизменяемый список
# 1 способ
colors = tuple() # не используем
# 2 способ
new_colors = ("red","blue")

# тип данных Словарь (объект в js)
car = {}
my_car = dict() # с помощью функции

# хранит данные в формате ключ значение ключ значение (не упорядоченно)
info = {"name": "Misha",
        age: 26,
        "city": "Moscow",
        25: 26,
        ("1",2,3) : 24
        }
# не может быть 2х одинаковых ключей
# ключом словаря может быть только неизменяемый тип данных (строка, int, кортеж). Т.е. переменная не м.б. ключом

# set множество
set_of_name = {"Masha", "Sasha", "Dima", "Masha"}
print(type(set_of_name))
print(set_of_name)

pop = ['bmw','audi','bmw','bmw']

# list  в set
print(set(cars))
print(list(set(cars)))

txt = "Hi"
print(set(txt))

# управляюще конструкции

# if - elif - else
age = 0
if age < 20:
    print("error") # отступ - часть кода (т.е. это команда)

print("next block")

if age < 11 and age !=0:
    print("error")
elif age == 0:
    print("age == 0")
else:
    print("ok")

in_name = input("Введите Ваше имя: ")
in_age = input("Введите Ваш возраст: ")

print (f"Ваше имя - {in_name}")
print(type(in_age))

print(12 =='12')