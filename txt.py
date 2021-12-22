
#открывает файл из того же места(целиком)
from os import read

s = open("2 февраля.py")
print(read(s))
s.close()

#перезаписывает файл и пишет Привет
s = open("фигня какая-то.py", 'w')
s.write('Привет')
s.close()

#добавляет в конец файла 'Привет'
s = open("фигня какая-то.py", 'a')
s.write('Привет')
s.close()

#комбо дозаписи и считывания
s = open("фигня какая-то.py", 'a')
s.write('Привет')
s.close()
s = open("фигня какая-то.py")
print(s.read())
s.close()
#нахождение уникальных слов в предложении через файлыт
s = open("tada.txt", "r")
text = s.read()

open("result.txt", "w", encoding = "utf - 8").close()
razd = text.split('.')
for i in razd:
temp = i.split()
temp2 = set(temp)
print(len(temp2))
s.close()
s = open("result.txt", "a")
s.write(str(len(temp2)) + "\n")
s.close()
s = open("result.txt", "r")
print(s.read())
s.close()