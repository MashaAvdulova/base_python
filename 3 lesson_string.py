# строки (string)
from google.protobuf.internal.test_bad_identifiers_pb2 import descriptor

name = 'Sasha'
lastname = 'Ivanov'
gender = 'm'

#1 вариант
text = ('dfjgdljgdzjg'
        'hfbgldshfgldfgl'
        'ldfsgjldsj')
# 2 вариант - создание переменной
descrition = '''
    jkljljlkj
    jljkljl
    hjfhj
    k'''
print(type(text))

car = 'bmw'
print(id(car))
print(car+ ' 3')
print(id(car))
car = car + ' 3'
print(id(car))
print(car)
car += 'x5'
print(car)

print(len(car))
print(car[0])
print(car[-1])
print(car[:3])

# возвращает id необходимого для поиска элемента
print(car.find('b'))
print(car.find('1')) # несуществующий элемент

if car.find('3') != -1:
    print('3')
elif car.find('5') != -1:
    print('5')
print(car)



print('aaaatjtrj'.count('aa')) # считает количество элементов
print('bmwx5'.index('x5')) # ищет начало подстроки (похоже на find), но выдает ошибку, если нет искомого элемента

name = 'dima'
print(name.title()) # первый символ в слове в первом регистре
print(name.upper()) # все символы в первом регистре
print('DIMA'.lower()) # все символы в первом регистре

print('dima ivanov'.title())
print('dima ivanov'.capitalize()) # первый символ строки
print('dima ivanov'[0].upper())

# первую букву заглавной
name_dima = 'dima ivanov'
print(name_dima[0].title()+name_dima[1:])


my_text = 'I Love love python'
print(my_text.lower().count('l')) # считаем количество l  и L


emails = [
    'user@mail.ru'
    'admin@gmail.com'
    'alex@yandex.ru'
]
for email in emails:
    if email.endswith('ru'): #  чем заканчивается
        print (email)

for email in emails:
    if email.startswith('admin'): #  с чего начинается
        print (email)

# метод проверяет является ли строка числом

a='26'
b='hello2'
print(a.isdigit())
print(b.isdigit())
print(b.isalpha()) # является ли текстом

age = '26a'
if age.isdigit():
    if int(age) < 30:
        print('ok')
else:
    print('Не является числом')


# преобразование строк в списки и наоборот
my_string = 'I love python'

# посчитать сколько слов строке
print(my_string.split()) # по умолчанию разделитьель - пробел, т.е. можно не писать

my_string = 'I---love---python'
print(my_string.split('-'))
print(my_string.split('---'))

my_string = ('I\nlove\npython') # перенос на новую строку
print(my_string.split('\n'))

# метод очищения строк
# strip

word = '!hello.'
print(word.strip('!.')) # передаем те символы, которые хотим очистить слева и справа
print(word.rstrip('!')) # справа

my_string = 'I,.love, python'
clean_list = []
for word in my_string.split(','):
    clean_list.append(word.strip('!. '))
print(clean_list)

my_list = ['mail', 'academy', 'ru']
# mail.academy.ru хотим получить

# 1 способ
site = ''
for word in my_list:
    site += word + '.'
site = site [:-1]
print(site)

# 2 способ
site = '.'.join(my_list) # соединяем элементы сприска через заданный разделитель
print(site)

new_string = ' - '.join(['bmw','audi', 'renault'])
print(new_string)
print(new_string.split(' - '))

stih = 'dfgdfgdg\ndfhdfhd\nfhdh'
print(stih.splitlines())