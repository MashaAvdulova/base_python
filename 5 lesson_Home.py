#  Задание 1
# 1. создайте текстовый файл task_1.txt при помощи python.
# 2. запишите в него следующий текст: Пословицы – неотъемлемая часть повседневной речи каждого Русского человека.
# 3. считайте файл в программу
# 4. Выведите на экран следуюущую информацию с пояснениями:
# - первый символ текста
# - последний символ текста
# - первые три символа
# - последние три символа
# - первое слово
# - последнее слово
# - количество символов
# - количество слов
# - тест в верхнем регистре
# - текст в нижнем регистре

lesson_5_task_1 = open('lesson_5_task_1.txt', 'w',  encoding = 'utf-8') # режим добавления к существующему файлу
text = 'Пословицы – неотъемлемая часть повседневной речи каждого Русского человека.'
lesson_5_task_1.write(text)
lesson_5_task_1.close()

lesson_5_task_1 = open('lesson_5_task_1.txt', 'r',  encoding = 'utf-8')
new_text= lesson_5_task_1.read()
print(f'Задание №1')
print(f'1. Первый символ текста - {new_text[0]}')
print(f'2. Последний символ текста - {new_text[len(new_text)-1]}')
print(f'3. Первые три символа - {new_text[:3]}')
print(f'4. Последние три символа - {new_text[-3:]}')
symbol = new_text.split()
word = []
for i in symbol:
    if str.isalpha(i[0]):
        word.append(i)
print(f'5. Первое слово - {word[0]}')
print(f'6. Последнее слово - {word[-1]}')
print(f'7. Количество символов - {len(new_text)}')
print(f'8. Количество слов - {len(word)}')
print(f'9. Текст в верхнем регистре - {new_text.upper()}')
print(f'10. Текст в нижнем регистре - {new_text.lower()}')

#  Задание 2
# Дан файл со стихотворением poem.txt.
# Необходимо провести анализ текста и результат вывести на экран с пояснениями.
#
# 1. Сколько всего символов в тексте
# 2. Сколько букв в тексте (без пробелов и знаков препинания (,.!?))
# 3. Сколько всего строк в тексте
# 4. Сколько непустых строк в тексте
# 5. Сколько всего слов в тексте
# 6*. Сколько слов в каждой строке
# 7*. Сколько символов в каждой строке
# 8. Найти повторяющиеся слова в тексте с указанием количества
# 9*. Провести частотный анализ букв (частота появления какждой буквы в тексте)
# 10. Найти все посторонние символы (пробелы и знаки препинания) - какие и сколько
#
# Пример вывода:
# 1. Всего символов в тексте - 670
# 2. Букв в тексте - 500
# 3. Всего строк в тексте - 40
# 4. Непустых строк в тексте - 30
# 5. Всего слов в тексте - 100
# 6. Анализ слов по строкам:
# 1 строка - 5 слов
# 2 строка - 4 слова
# 3 строка - 6 слов
# ....
# 7. Анализ символов по строкам:
# 1 строка - 25 символов
# 2 строка - 16 символов
# ....
# 8. Повторяющиеся слова:
# как - 2
# и - 8
# а - 6
# или - 3
# 9. Частотный анализ текста:
# а - 34
# б - 27
# в - 15
# г - 13
# ...
# 10. Прочие символы:
# пробелов - 56
# . - 16
# , - 34
# - - 25
# : - 4

poem = open('poem.txt', 'r',  encoding = 'utf-8')
text_poem = poem.read()

print(f'Задание №2')

# 1. Сколько всего символов в тексте
print(f'1. Всего символов в тексте - {len(text_poem)}')

# 2. Сколько букв в тексте (без пробелов и знаков препинания (,.!?))
num_znak = 0
for i in text_poem:
    if (i ==',') or (i =='.') or  (i =='!') or (i =='?') or (i =='-') or (i ==':')  or (i ==';')   or (i ==' '):
        num_znak = num_znak + 1
print(f'2. Букв в тексте - {len(text_poem) - num_znak}')

# 3. Сколько всего строк в тексте
num_str = text_poem.split('\n')
print(f'3. Всего строк в тексте -  {len(num_str)}')

# 4. Сколько непустых строк в тексте
num_str_empty = 0
for i in num_str:
    if i == '':
        num_str_empty = num_str_empty + 1
print(f'4. Непустых строк в тексте -  {len(num_str) - num_str_empty}')

# 5. Сколько всего слов в тексте
symbol_poem = text_poem.split()
word_poem = []
for i in symbol_poem:
    word = i.strip(',.?!;:-')
    word_poem.append(word)
print(f'5. Всего слов в тексте -  {len(word_poem)}')

# 6*. Сколько слов в каждой строке
print(f'6. Анализ слов по строкам:')
for i in range(len(num_str)):
    symbol_str_poem = num_str[i].split()
    word_str_poem = []
    for j in symbol_str_poem:
        word = j.strip(',.?!;:-')
        word_str_poem.append(word)
    print(f'{i+1} строка -  {len(word_str_poem)} слов/слова')

# 7*. Сколько символов в каждой строке
print(f'7. Анализ символов по строкам:')
for i in range(len(num_str)):
    print(f'{i+1} строка -  {len(num_str[i])} символов/символ')

# 8. Найти повторяющиеся слова в тексте с указанием количества
print(f'8. Повторяющиеся слова: ')
text_poem_lower = text_poem.lower()
text_poem_sp = text_poem_lower.split()
text_poem_clean =[]
for i in text_poem_sp:
    word = i.strip(',.?!;:-')
    text_poem_clean.append(word)
text_poem_set = set(text_poem_clean)
for i in text_poem_set:
    num = text_poem_clean.count(i)
    if num > 1:
        print(f'{i} - {num}')

# 9*. Провести частотный анализ букв (частота появления каждой буквы в тексте)
# 10. Найти все посторонние символы (пробелы и знаки препинания) - какие и сколько

letters = list(text_poem_lower)
letters_uniq = list(set(letters))
letters_uniq.sort()
print(f'9. Частотный анализ текста:')
for i in letters_uniq:
    num = letters.count(i)
    if i.isalpha():
       print(f'{i} - {num}')
print(f'10. Прочие символы:')
for i in letters_uniq:
    num = letters.count(i)
    if i.isalpha():
        break
    else:
        print(f'{i} - {num}')
