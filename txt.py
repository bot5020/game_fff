
#��������� ���� �� ���� �� �����(�������)
from os import read

s = open("2 �������.py")
print(read(s))
s.close()

#�������������� ���� � ����� ������
s = open("����� �����-��.py", 'w')
s.write('������')
s.close()

#��������� � ����� ����� '������'
s = open("����� �����-��.py", 'a')
s.write('������')
s.close()

#����� �������� � ����������
s = open("����� �����-��.py", 'a')
s.write('������')
s.close()
s = open("����� �����-��.py")
print(s.read())
s.close()
#���������� ���������� ���� � ����������� ����� ������
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