from functools import reduce
# импортируем функцию reduce из встроенной библиотеки functools (внутренняя библ)

# Функции
def get_sum_numbers(): # ничего не принимает
    a = 5
    b = 6
    print(a+b) # не возвращает значение print
    return # = ничего не писать / return None - прерывает выполнение функции

get_sum_numbers() # вызываем функцию
print(get_sum_numbers())

# позиционные параметры функции
def get_sum_numbers_2(num_1,num_2):
    print(num_1 + num_2)
a = 10
b = 10
get_sum_numbers_2(a,b)
get_sum_numbers_2(20,20)


# возвращаем результат функции
def get_sum_numbers_3(num_1,num_2):
    return num_1 + num_2
print(get_sum_numbers_3(30,30))

c= get_sum_numbers_3(40,40) # заносим значение в переменную
print(c)

# параметры : get_sum_numbers_3(num_1,num_2) (аргументы:get_sum_numbers_3(a,b))
# -позиционные
# -именованные

# значение по умолчанию
def get_sum_numbers_4(num_1,num_2=0):
    return num_1 + num_2
print(get_sum_numbers_4(num_1=50,num_2=50))


def get_first_last_char(text):
    first = text[0]
    last = text[-1]
    second = text[1]
    return first, last, second
# 1
result = get_first_last_char(text='python')
print(result) # значение вернулись в кортеж, если функция возвращает более одного значения
print(result[0])
print(result[1])
# 2
a, b, c = get_first_last_char(text='python')
print(a)
print(b)
# 3
_,_, second = get_first_last_char(text='python')
print(second)


# pass оператор "заглушки"
# def get_max_value(number):
#     pass

def get_max_value(numbers):
    max_val = numbers[0]
    for i in numbers:
        if i > max_val:
            max_val = i
    return max_val
nums = [1,9,6,8,7]
max_v = get_max_value(nums)
print(max_v)

def get_min_value(numbers):
    min_val = numbers[0]
    for i in numbers:
        if i < min_val:
            min_val = i
    return min_val

min_v = get_min_value(nums)
print(min_v)

def get_sum_even_numbers(numbers):
    sum_ = 0
    for i in numbers:
        if i%2 == 0:
            sum_ += i
    return sum_

sum_numbers = get_sum_even_numbers(numbers=nums)
print(sum_numbers)


text = 'I,Love - Python'

# вернуть список [i, love, python]
def get_clean_words(text):
    text = text.replace(',', ' ').replace('-', '').lower().split()
    return text
text_clean = get_clean_words(text)
print(text_clean)

# анонимные функции: lambda-функции для создания простых выражений
# 1
def hello():
    print('hello')

message = lambda: print('hello')
message()

#2
def square(x):
    return x*x

square_ = lambda x: x*x
print(square_(2))

# 3
def sum_num(a,b):
    return a+b

sum_ = lambda x, y: x+y
print(sum_(2,3))


# функции высшего порядка - принимают в качестве параметра др.функции
# map - применяется для преобразования элементов, применяя к каждому элементу заданную функцию
#
numbers = [1,2,3,4,5]
squared_numbers = list(map(square, numbers)) # square без скобок () - ссылка на функцию
print(squared_numbers)
list() # преобразование в список
squared_numbers_l = list(map(lambda x: x*x, numbers))

# 2
list_of_words = ['AAA', 'BBB']
lower_word = list(map(lambda x: x.lower(), list_of_words))
print(lower_word)

# filter - используется для фильтрации,
# оставляя только те, для которых заданная функция возвращает true

def is_even(x): # возвращаем значение true false
    return x%2 == 0

numbers_2 = [1,2,3,4,5,6,7,8,9]
even_numbers = list(filter(lambda x: x%2 ==0, numbers_2))
print(even_numbers)

# reduce - для последовательного применения функции к элементам
# и сводит к единственному значению

# 1
sum_of_numers = reduce(lambda x, y : x+y, numbers_2, 3) # 3 - начальное значение, функция такова, что она использует 2 элемента: текущее и следующее
print(sum_of_numers)

# 2

# Предварительно
x = 5
y = 8
if x<y:
    print(x)
else:
    print(y)

print(x if x<y else y)
print(x**2 if x<y else y*8)

# reduce
min_value = reduce(lambda x,y: x if x<y else y, numbers_2)
print(min_value)