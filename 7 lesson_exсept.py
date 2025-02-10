import  os

#  обработка ошибок
# 1 пример
age = input ('Введите возраст: ')
try:
    if age < 21:
        print('Не разрешено')
except TypeError as err: # TypeError указываем тип ожидаемой ошибки, err - создаем переменную и связываем с ней ошибку
    # если запускается этот блок, то ничего из блока try не выполнится
    print('Возникла ошибка')
    print(err)
except ValueError as type_err:
    print('Неверный тип значения')
    print(type_err)
finally: # необязательная часть - продолжение в любом случае. Исп.редко
    print('Текст после блока обработки')

# 2 пример
def get_card_price(sku):
    pass

def get_sale_price(sku):
    pass

def get_product_info(sku):
    try:
        card_price = get_card_price(sku)
    except Exception as arr: # Exception - любой тип ошибки, но лучше его не использовать
        card_price = 0
    try:
        sale_price = get_sale_price(sku)
    except Exception as arr:
        sale_price = 0
    info = {
        'card_price': card_price,
        'sale_price': sale_price
    }

#1 вариант открытия файла
file = open ('My file.txt', 'r', encoding='utf-8')
text = file.read()
file.close()
print(text)

# 2 вариант. Контекстное соединение
try:
    with open('My file2.txt', 'r', encoding='utf-8') as file: # с открытием файла связать переменную. My file2 yне существует
        text = file.read() # при выходе из данного блока файл закроется автоматически
        print(text)
except FileNotFoundError as err:
    print(f'Ошибка: {err}')
    text ='!!!'
    print(text)

with open('My file.txt', 'w', encoding='utf-8') as file:
    text = file.write('!!!')
print(text)

if os.path.isfile('My file2.txt'):
    with open('My file2.txt', 'r', encoding='utf-8') as file:
        text = file.read()
else:
    print ('Файла нет')



# 3 пример. Генерируем исключения
def validate_age(age):
    if age < 21:
        raise ValueError('Неверный возраст!')
    return age

def get_person_info(info):
    print(info)

age = int(input('Введите возраст: '))
try:
    age = validate_age(age)
except ValueError:
    print('Запись ошибки в журнал')
    age = 0

info = {'name': 'Alisa', 'age': age}
get_person_info(info)

# 4 пример
while True:
    age = int(input('Введите возраст: '))
    try:
        age = validate_age(age)
        info = {'name': 'Alisa', 'age': age}
        get_person_info(info)
        break # выход из бесконечного цикла
    except ValueError as err:
        print(err)