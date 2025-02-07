from functools import reduce
# 1. Написать функцию, которая возвращает факториал числа
num = int(input('Введите число для расчета факториала '))
num_sp = list(range(num+1))
num_sp.pop(0)
num_fact = reduce(lambda x, y : x*y, num_sp)
print(f'Факториал {num} равен {num_fact}')

# 2. Написать функцию, которая принимает строку и возвращает количество символов в ней
str = input('Введите текст ')
print(f'Количество символов во введенном тексте - {len(str)}')

# 3. Написать функцию, которая принимает имя, фамилию, возраст и возвращает словарь с этими данными
def person():
    person = {}
    person['name'] = input('Введите Ваше имя ')
    person['surname'] = input('Введите Вашу фамилию ')
    person['age'] = input('Введите Ваш возраст ')
    return person
print(person())

# 4. Написать функцию, которая принимает 3 числа и возвращает словарь,
#    в котором содержится информация о сумме этих чисел, максимальном числе, минимальном числе
def numbers():
    result = {}
    a = int(input('Введите число a '))
    b = int(input('Введите число b '))
    c = int(input('Введите число c '))
    numbers =[a,b,c]
    result['sum'] = a+b+c
    result['max'] = reduce(lambda x,y: x if x>y else y, numbers)
    result['min'] = reduce(lambda x,y: x if x<y else y, numbers)
    return result
print(numbers())
