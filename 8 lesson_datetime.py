from datetime import datetime
from datetime import timedelta

today = datetime.today()
print(today)
print(type(today))
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)

# форматирование объекта datetime в строку определенного формата
f_date = today.strftime('%d - %m - %Y %H:%M:%S') # меняем форму вывода дата время. Тип данных - строка
current_time = today.strftime('%H:%M:%S')
print(f_date)
print(current_time)

# форматиррование строки с датой (и времение) в объект datetime
birth_day = '13.04.1982'
birth_day_dt = datetime.strptime(birth_day, '%d.%m.%Y')
print(birth_day_dt, type(birth_day_dt))
print(birth_day_dt.weekday())

# арифметические операции с датами
# добавить к дате 5 дней
future_day = today + timedelta(days=5)
print(future_day)

first_day = '01.01.2025'
second_day = '20.01.2025'
first_day_dt = datetime.strptime(first_day, '%d.%m.%Y')
second_day_dt = datetime.strptime(second_day, '%d.%m.%Y')

delta = second_day_dt - first_day_dt
print(delta)
print(delta.days)

"""
1. Написать функцию, которая возвращает, сколько дней осталось до нового года
2. Написать функцию, которая принимает дату рождения и возвращает количество полных лет
3. Написать функцию check_date(), которая принимает дату в формате строки "дд.мм.гггг" 
и возвращает количество дней, которые прошли с этой даты или сколько дней осталось)

4. 
4.1 Написать функцию, которая принимает информацию о книге из консоли (автор, название, год, жанр)
4.2 Написать функцию, которая сохраняет в словарь информацию о книге с валидацией года
    (1500 < год < текущий)
4.3 Сохранить в новый словарь информацию о 5 книгах
    {
	"1": {
		"author": "Pushkin",
		"title": "Ruslan & Ludmila",
		....
	},
	"2": ...

    }
4.5 Записать информацию о 5 книгах в books.json
4.6 Считать инф-ю из books.json в консоли
"""