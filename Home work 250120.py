# Задание
# 1. Написать программу, которая выводит на экран список четных чисел от 10 до 30.

for i in range(10,31):
    if i%2 ==0:
        print(i)

# 2. Написать программу, которая принимает от пользователя ввод трех имен и добавляет их в список names
# Выведите список на экран
# Выведите количество элементов списка
# Выведите отдельно первый элемент списка
# Выведите отдельно последний элемент списка

names = []
while len(names) < 3:
  new_name = input("Введите имя ")
  names.append(new_name)
print(names)
print(len(names))
print(names[0])
print(names[2])


# 3. в получившийся во 2 задании список names добавьте имя Igor во 2 позицию
# выведите на экран индекс этого элемента
# удалите имя Igor из списка

names.insert(1, 'Igor')
print(names)
print(names.index('Igor'))
names.remove('Igor')
print(names)
