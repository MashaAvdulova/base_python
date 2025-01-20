# списки
names = []

# дробавление элемента в конец списка
names.append (2)
names.append('Alex')
my_name = 'Elena'
names.append(my_name)
print(names)

# получить элемент списка (с удалением его из списка)
last_name = names.pop(0)
print(last_name)
print(names)

# подсчет кол-ва элемента в списке
print(names.count('24r1212'))

# поиск первого индекса элемента
names.append('Alex')
print(names)
ind = names.index('Alex', 1, 3)
print(ind)

# добавление элемента в произвольное место списка
names.insert(0, 'Masha')
print(names)

# удаление элемента из списка по его значению (элемент не возвращается)
names.remove('Alex')
print(names)

# подсчет кол-ва элементов
print(len(names))

# получение элементов списка (только по индексу)
print(names[0])
print(names[1])
print(names[-1]) # выводит последний элемент. -2 -3 ...

# срезы списка
print(names[0:2]) # левая граница вкл., правая -нет
print(names[:2]) # от начала до 2го
print(names[1:])

names.extend(['Dima', 'Vova', 'Sergey']) # расширение списка на список
print(names[1:4:1]) # с 1 по 3 с шагом 1
print(names[5:1:-1]) # с 5 по 2 с шагом 1
print(names)
print(names[::-1])

# цикл For
for i in names:
    print(i)

# range(6) = (0,1,2,3,4,5)
# range(1,5) = (,1,2,3,4,)
for i in range(len(names)):
    print(f"{i+1}. {names[i]}")

a = 5
a = a +1
a += 1

a = 10
while a>0:
    print("Hello")
    a -=1
    if a == 4:
        break # принудительный выход из цикла

# while True: # бесконечный цикл
#     print ('Выберите действие:')
#     print ('1. Добавить книгу')
#     print ('2. Удалить книгу')
#     print ('Введите 0 для выхода из меню')
#
#     action = input('>>> ')
#     if action == '1':
#         print('Книга добавлена')
#     elif action == '2':
#         print('Книга удалена')
#     elif action == '0':
#         print('До свидания')
#         break
#     else:
#         print('Выберите нужный пункт меню')

print(names)
names += ['Nasya', 'Olga'] # как extend
print(names)
names.append(['Nasya', 'Olga'])
print(names)

for i in range(9):
    print(i+1)

for i in range(1,10):
    print(i)

a = 1
while a<=9:
    print(a)
    a +=1

# кортеж
# tuple

numbers = (1,2,3,4)
status = (
    ('in_process', 'В работе'),
    ('success', 'Выполнено'),
)

print(len('Dima')) # функция. Работает с объектом в скобках
# names.append() # метод - функция внутри класса

# словарь. Данные в формате ключ - значение
person = {}
info = {'name': 'Dima', 'age': 26} # переменные без кавычек

# получение элемента словаря (значение по ключу)
name =  info ['name']
print(info['name'])

# добавление элемента в словарь
info ['phone'] = '89112223344'
# обновление значения элемента
info ['name'] = 'Sergey'
print(info)

# размер словаря равен кол-ву элементов (пар, ключей)
print(len(info))
info ['leng'] = ['russian', 'english']
print(info)

info ['edu'] = {'hight': 'MGU', 'medium': 'ITMO'}
print(info)

# ключом м.б. только неизм.тип данных (строка, число, кортеж)
cars = {('bmw', 'audi'): 'germany'}

age = info.pop('age')
print(age)
print(info)

print(info.get('age', {}))

print(info.get('edu', {}))
print(info.get('edu', {}).get ('hight', {}))
print(info.get('edu', {}).get ('hight2', {})) # получение ключа, если данные есть, и присвоение нулевого значения, если данных по ключу нет  (ключа не существует)

print(info)
info_copy = info # копируется ссылка на одну и ту же ячейку памяти. Т.е. меняем один словарь, меняется и др
print(info_copy)
print(id(info))
print(id(info_copy))

new_info = info.copy() # создаем новый объект в памяти
print(id(info))
print(id(new_info))


# users =[]
# info_person = {}
# for i in range(3):
#     name = input ('Введите имя')
#     phone = input ('Введите телефон')
#     info_person['name'] = name
#     info_person['phone'] = phone
#     users.append(info_person)
# print(users)

# users =[]
# info_person = {}
# for i in range(3):
#     name = input ('Введите имя')
#     phone = input ('Введите телефон')
#     info_person['name'] = name
#     info_person['phone'] = phone
#     users.append(info_person.copy())
# print(users)


# users =[]
# for i in range(3):
#     name = input ('Введите имя')float8
#     break
#     phone = input ('Введите телефон')
#     info_person = {'name': name, 'phone': phone}
#     users.append(info_person)
# print(users)

print(list(info.keys()))
print(list(info.values()))
print(list(info.items())) # выдает пару ключ-значение
info.update({'name': 'gdfgdg', 'age': 12321}) # расширение с обновление существующего

for i in info: # = info.keys
    print(i)

for key in info: # = info.keys
    print(f'{key} - {info[key]}')

for key, value in info.items(): # = info.keys
    print(f'{key} --- {value}')

