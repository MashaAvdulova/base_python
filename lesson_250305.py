from curses.ascii import isalpha

# Напишите функцию, которая принимает строку и проверяет,
# является ли строка автомобильным номером формата А123АА198
# Функция должна возвращать True или False
def islatinic(s:str):
    list_of_sim = 'авекмнозстухabekhoc'
    if s.lower() in list_of_sim:
        return True
    return False

def isnumber():
    number = input('Введите номер автомобиля в формате А123АА198 или А123АА98: ')
    if len(number)==9 or len(number)==8:
        print(islatinic(number[0]) & islatinic(number[4]) & islatinic(number[5]) & number[1:3].isdigit() & number[6:].isdigit())
    else: print('Некорректно введен номер')
isnumber()

# ** Напишите программу которая выводит на экран сумму чисел от 20 до 30
def summ():
    summ = 0
    for i in range(20,31):
        summ += i
    return summ
print(summ())

# ** Напишите программу которая выводит на экран сумму четных чисел от 10 до 20
def summ_chet():
    summ_chet = 0
    for i in range(10,21):
        if i%2 == 0:
            summ_chet = summ_chet + i
    return summ_chet
print(summ_chet())

# ** Напишите программу, которая получает от пользователя строку и выводит на экран
# 1 и последний символ строки, а также количество символов строки
def string():
    string = input('Введите символы строки: ')
    print(string[0])
    print(string[len(string)-1])
    print(len(string))
string()