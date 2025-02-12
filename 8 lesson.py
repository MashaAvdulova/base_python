import json

# валидация возраста



def validate_age(age: str) -> int: # age: str указываем ожидаемый тип переменной (для удобства написания кода). -> int или указываем формат значения, которое возвращает
    if age.isdigit():
        if 0<int(age)<150:
            return int(age)
        else:
            raise ValueError('Возраст должен быть от 1 до 150')
    else:
        raise TypeError('Возраст должен быть числом от 1 до 150')

# валидация номера телефона
def validate_phone(phone) -> str:
    numbers =[]
    if isinstance(phone, str): # проверяем тип phone является ли str
        if len(phone) == 11 or len(phone) == 15:
            for i in phone:
                if i.isdigit():
                    numbers.append(i)
            if len(numbers) == 11:
                return phone
            else:
                raise ValueError('Неверный формат телефона')
        else:
            raise ValueError('Неверный формат телефона')
    else:
        raise ValueError('Неверный формат телефона')

# получение данных от пользователя
def get_user_info() -> tuple[str, str, str]: # несколько параметров возвращаютсмя автоматически в виде картежа
    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    phone = input('Введите номер телефона: ')
    return name, age, phone

# создание объекта пользователя
def create_user(name: str, age: str, phone: str):
    name = name.capitalize()
    age = validate_age(age)
    phone = validate_phone(phone)

    info = {
        'name': name,
        'age': age,
        'phone': phone
    }
    return  info

# сериализация (объект Puthon-> json)
def write_user_info(info: dict):
    with open('8 lesson_info.json', 'w', encoding='utf-8') as file:
        json.dump(info, file, indent=2, ensure_ascii=False) # количество отступов при записи, ensure_ascii=False - русский текст правильно передается
        # json формат для передачи данных

# десериализация (объект json -> Puthon)
def read_user_info():
    with open('8 lesson_info.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def main():
    users = {}
    user_info = get_user_info() # (dima, 22 , 89999999999) = dima, 22 , 89999999999
    user = create_user(*user_info) # * =означает распаковку в виде выше
    for i in range(10):
        users[i] = user
    write_user_info(users)

    data = read_user_info()
    print(data)
    print(type(data))

# запускать файл, только если он запущен как главный (не в момент импорта на других страницах)
if __name__ == '__main__':
    main()