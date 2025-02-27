from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import json

# 1. Написать функцию, которая возвращает, сколько дней осталось до нового года
today = datetime.today()
new_year_year = today.year
new_year_first_day = datetime.strptime(f'01.01.{new_year_year+1}', '%d.%m.%Y')
delta = new_year_first_day - today
print(delta)

# 2. Написать функцию, которая принимает дату рождения и возвращает количество полных лет
birthday = input('Введите дату рождения: ')
birthday_dt = datetime.strptime(birthday, '%d.%m.%Y')
age = relativedelta(today, birthday_dt).years
print(age)

# 3. Написать функцию check_date(), которая принимает дату в формате строки "дд.мм.гггг"
# и возвращает количество дней, которые прошли с этой даты или сколько дней осталось)
def check_date():
    date = input('Введите дату в формате "дд.мм.гггг": ')
    date_dt = datetime.strptime(date, '%d.%m.%Y')
    days = date_dt - today
    num = days.days
    if num > 0:
        print(f'До указанной даты осталось {num} дней')
    elif num < 0:
        print(f'От указанной даты прошло {-num} дней')
    else:
        print(f'Вы ввели сегодняшнюю дату')
check_date()

# 4.
# 4.1 Написать функцию, которая принимает информацию о книге из консоли (автор, название, год, жанр)
def get_book_info() -> tuple[str, str, str, str]: # несколько параметров возвращаютсмя автоматически в виде картежа
    print('Введите информацию о книге')
    author = input('Автор: ')
    title = input('Название: ')
    year = int(input('Год издания: '))
    style = input('Жанр: ')
    return author, title, year, style

# 4.2 Написать функцию, которая сохраняет в словарь информацию о книге с валидацией года
#     (1500 < год < текущий)
def create_book(author: str, title: str, year: int, style: str):
    if (year < 1500) | (year > new_year_year):
        raise ValueError('Год выпуска должен быть от 1500 до текущего года')
    else:
        info = {
            'author': author,
            'title': title,
            'year': year,
            'style': style
        }
    return info

# 4.3 Сохранить в новый словарь информацию о 5 книгах
#     {
# 	"1": {
# 		"author": "Pushkin",
# 		"title": "Ruslan & Ludmila",
# 		....
# 	},
# 	"2": ...
#
#     }
def create_books():
    books = {}
    for i in range(5):
        book_info = get_book_info()
        book = create_book(*book_info)
        books[i+1] = book
    return books
books = create_books()


# 4.5 Записать информацию о 5 книгах в books.json
def write_book_info(books: dict):
    with open('Home work 250212_info.json', 'w', encoding='utf-8') as file:
        json.dump(books, file, indent=2, ensure_ascii=False)
write_book_info(books)

# 4.6 Считать инф-ю из books.json в консоли
def read_book_info():
    with open('Home work 250212_info.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

data = read_book_info()
print(data)