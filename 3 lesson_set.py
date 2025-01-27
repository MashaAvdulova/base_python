# тип данных множество - set() - {}

# создание множества при помощи литерала
set_of_numbers = {1,2,2,2,3,4}
print(type(set_of_numbers))
print(set_of_numbers)

names = ['Ivan', 'Maria', 'Ivan']
print(set(names)) # преобразование в тип множество ['Ivan', 'Maria']

# создание множеств при помощи литералов
set_of_names = set (['Ivan', 'Maria', 'Ivan'])
print (set_of_names)
print (len(set_of_names))

# добавление элемента во множество
set_of_names.add('Dima')
print(set_of_names)

# удаление элемента из множества
set_of_names.remove('Dima')
print(set_of_names)

# проверим, есть ли элемент во множестве. Если есть удалим
# in проверяет вхождение элемента в коллекцию
if 'Dima2' in set_of_names:
    set_of_names.remove('Dima')
else:
    print('Такого элемента нет')

set_of_names.discard('Dima2')
print(set_of_names)

# объединение множеств (1 способ)
users_1 = {"Dima","Vova","Elena"}
users_2 = {"Dima","Sasha","Masha"}

users_3 = users_1.union(users_2)
print(users_3)

# операция логического сложения (2 способ)
users_1 = {"Dima","Vova","Elena"}
users_2 = {"Dima","Sasha","Masha"}
users_3 = users_1 | users_2
print(users_3)

# пересечение множеств
users_1 = {"Dima","Vova","Elena"}
users_2 = {"Dima","Sasha","Masha"}
users_3 = users_1.intersection(users_2)
print(users_3)

# & операция логического умножения
users_1 = {"Dima","Vova","Elena"}
users_2 = {"Dima","Sasha","Masha"}
users_3 = users_1 & users_2
print(users_3)

# сразу заменяем первое множество
users_1 = {"Dima","Vova","Elena"}
users_2 = {"Dima","Sasha","Masha"}
users_1.intersection_update(users_2)
print(users_1)

# разность множеств
users_1 = {"Dima","Vova","Elena"}
users_2 = {"Dima","Sasha","Masha"}
users_3 = users_2.difference(users_1)
print(users_3)

# симметрическя разность (исключающее или)
# 1 сп
users_1 = {"Dima","Vova","Elena"}
users_2 = {"Dima","Sasha","Masha"}
users_3 = users_1.symmetric_difference(users_2)
print(users_3)

# 2 сп
users_1 = {"Dima","Vova","Elena"}
users_2 = {"Dima","Sasha","Masha"}
users_3 = users_1 ^ users_2
print(users_3)

# делает множество неизменяемым
users_4 = frozenset({"Masha","Sasha"})
print(type(users_4))
users_3 = frozenset(users_3) # делаем users_3 неизменяемым
print(type(users_3))
users_3 = set(users_3) # возвращаем обратно в тип множество
print(type(users_3))

