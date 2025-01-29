# чтение файла
# можно открыть только существующий файл

# открытие в режиме чтения
myfile = open('My file.txt','r', encoding = 'utf-8') # путь к файлу (относительно файла запуска, режим запуска
# encoding = 'utf-8' - для работы Windows

text = myfile.read() # считываем файл, чтобы достать данные из него
myfile.close() # закрываем файл
print(text)
print(len(text))
print(text.splitlines())
print(len(text.splitlines()))

# создать файл в режиме записи
new_file = open('new_file.txt', 'w',  encoding = 'utf-8')
#new_file.read() ошибка, т.к. создали в режиме перезаписи файла после закрытия( т.е. каждый раз заново создается), а хотим открыть в режиме чтения
text = 'I love python'
new_file.write(text)
new_file.write(text+'\n')
new_file.write('\nPython forever\n')


# списки и словари:
name = ['Masha','Sasha', 'ivan']
for word in name:
    new_file.write(word + '\n')

names_string = '\n'.join(name)
new_file.write(names_string + '\n')

new_file = open('new_file.txt', 'a',  encoding = 'utf-8') # режим добавления к существующему файлу