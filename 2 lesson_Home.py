# 1. Напишите программу, которая принимает от пользователя его имя, фамилию, отчество, дату рождения и город.
# Запишите эти данные в словарь. В цикле выведите их со словаря на экран. Отдельно выведите фамилию и имя
info = {}
name = input("Введите Ваше имя ")
surname = input("Введите Вашу фамилию ")
patronymic = input("Введите Ваше отчество ")
birth = input("Введите дату Вашего рождения ")
city = input("Введите Ваш город ")
info ['name'] = name
info ['surname'] = surname
info ['patronymic'] = patronymic
info ['birth'] = birth
info ['city'] = city
for key, value in info.items():
    print(f'{key} - {value}')
print(f'Имя - {info["name"]}')
print(f'Фамилия - {info["surname"]}')


# 2. Напишите программу, которая циклом формирует числа от 0 до 30. Запишите эти цифры в список
num = []
for i in range(31):
    num.append (i)
print(num)


# 3. Дан список [1,30,30,25,24,30,1,27,25,40]. Выведите на экран только уникальные числа этого списка.
nums = [1,30,30,25,24,30,1,27,25,40]
uniq = []
for i in nums:
    if i not in uniq:
        uniq.append(i)
print(uniq)

# Создайте новый список и добавьте в него только числа большие 24. Выведите его на экран.
bigger24 = []
for i in uniq:
    if i > 24:
        bigger24.append(i)
print(bigger24)

# Создайте словарь, в котором ключами являются порядковые номера элементов, а значениями этих ключей четные цифры со второго списка.
# Например, {‘1’: 24, ‘2’: 28, ‘3’: 30}
num_box = {}
for i in range(len(uniq)):
    num_box [i+1]= uniq[i]
print(num_box)

# 4. Напишите программу, которая принимает на вход имя и возраст пользователя и выводит одно из двух сообщений на экран в зависимости от того,
# является ли пользователь совершеннолетним.
# Сообщения следующего вида: “Здравствуйте, имя_пользователя, вход разрешен!” или
# “Вам возраст_пользователя лет! Доступ запрещен” (Слова курсивом - значения соответствующих переменных, которые ввел пользователь)

name_a = input("Введите Ваше имя ")
age_a = int(input("Введите Ваш возраст "))
if age_a >= 18:
    print(f'Здравствуйте, {name_a}, вход разрешен!')
elif 1< age_a < 18:
    print(f'Вам {age_a} лет! Доступ запрещен')
else:
    print(f'Ошибка ввода данных')


# 5. Напишите программу, которая выводит на экран сумму чисел от 0 до 50 (1+2+3+...+50) при помощи цикла
sum = 0
for i in range(51):
    sum = sum + i
print(sum)


# 6. При помощи цикла выведите на экран все четные числа от 0 до 20 (% - операция получения остатка, например 5%2 = 1, 4%2=0.
# Проверка на равенство операция ==)
chet = []
for i in range(21):
    if (i+1)%2 == 0:
        chet.append(i+1)
print(chet)


# 7. Дан словарь d = {'1': 1.29, '2': 0.43}. Используя доступ к элементам словаря по ключу, найдите произведение 1.29*0.43,
# после чего добавьте результат в словарь, а затем выведите значение нового элемента на экран.
d = {'1': 1.29, '2': 0.43}
p = d['1'] * d['2']
print(p)


# 8. Напишите программу, которая запрашивает информацию о трех пользователях: имя, фамилия, телефон.
# Информацию об одном пользователе необходимо хранить в словаре, а информацию обо всех пользователях - в списке.
# (Должен получится список, состоящий из трех словарей, каждый из которых содержит информацию о пользователе)
users = []
for i in range(3):
    name = input("Введите Ваше имя ")
    surname = input("Введите Вашу фамилию ")
    phone = input("Введите Ваш телефон ")
    user = {'name': name, 'surname': surname, 'phone': phone}
    users.append(user)
print(users)

