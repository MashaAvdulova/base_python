import sys

month = input('Введите месяц: ')
match month:
    case '1':
        print('январь')
    case '2':
        print('февраль')
    case '3':
        print('март')
    case '4':
        print('апрель')
    case '5':
        print('май')
    case '6':
        print('июнь')
    case '7':
        print('июль')
    case '8':
        print('август')
    case '9':
        print('сентябрь')
    case '10':
        print('октябрь')
    case '11':
        print('ноябрь')
    case '12':
        print('декабрь')
    case _:
        print('неверный номер месяца')



def main_menu():
    text = '''
    1. Показать книгу\n
    2. Добавить книгу\n
    3. Найти книгу\n
    0. Выйти
    '''
    print(text)

def process_menu():
    action = input('>>> ')
    return action

def show_books():
    with open('7 lesson Books.txt', 'a+', encoding='utf-8') as file:
        file.seek(0) # перемещение курсора в начало файла при считывании
        books = file.read()
    if not books:
        print('Книг нет')
    else:
        print(books)

def add_books(): # уровень интерфеса (функция уровня интерфейса)
    author = input('Введите автора ')
    title = input('Введите название книги ')
    year = input('Введите год издания ')
    book = f'{author} - {title} - {year}'
    return book

def write_book_to_file(book): # функция уровня баз данных
    with open('7 lesson Books.txt', 'a+', encoding='utf-8') as file:
        file.write(book+ '\n')


def search_books():
    print('Поиск книги')

while True:
    main_menu()
    action = process_menu()
    match action:
        case '1':
            show_books()
        case '2':
            book = add_books()
            write_book_to_file(book)
        case '3':
            search_books()
        case '0':
            sys.exit() # выход из программы
        case _:
            print('Неверный пункт')
