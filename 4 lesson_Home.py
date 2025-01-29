# Пользователь с клавиатуры вводит текст. Запишите этот текст в файл text1.txt.
file_1 = open('4 lesson_Home.txt', 'w',  encoding = 'utf-8')
text = input('Введите Ваш текст ')
file_1.write(text+'\n')

# Пользователь с клавиатуры вводит текст. Добавьте этот текст в конец файла text1.txt
file_2 = open('text1.txt', 'a',  encoding = 'utf-8')
text = input('Введите Ваш текст ')
file_2.write(text+'\n')

# Выведите на экран содержимое файла text1.txt
file_2 = open('text1.txt', 'r',  encoding = 'utf-8')
print(file_2.read())
file_2.close()
