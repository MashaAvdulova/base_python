from datetime import datetime
from datetime import timedelta

# 1. Написать функцию, которая возвращает, сколько дней осталось до нового года
today = datetime.today()
new_year_year = today.year
new_year_first_day = datetime.strptime(f'01.01.{new_year_year+1}', '%d.%m.%Y')
delta = new_year_first_day - today
print(delta)

# 2. Написать функцию, которая принимает дату рождения и возвращает количество полных лет
birthday = input('Введите дату рождения: ')
birthday_dt = datetime.strptime(birthday, '%d.%m.%Y')
today_year = today.year
birthday_dt_year = birthday_dt.year
age = today - birthday_dt
print(today_year)
print(birthday_dt_year)
print(age.days)
print(age)

# 3. Написать функцию check_date(), которая принимает дату в формате строки "дд.мм.гггг"
# и возвращает количество дней, которые прошли с этой даты или сколько дней осталось)
#
# 4.
# 4.1 Написать функцию, которая принимает информацию о книге из консоли (автор, название, год, жанр)
# 4.2 Написать функцию, которая сохраняет в словарь информацию о книге с валидацией года
#     (1500 < год < текущий)
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
# 4.5 Записать информацию о 5 книгах в books.json
# 4.6 Считать инф-ю из books.json в консоли