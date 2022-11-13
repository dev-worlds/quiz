""" Module 4"""

age = 1799
answer = None

while answer != age:
    answer = int(input('Введите год рождения А.С Пушкина: '))
    if age == answer:
        print('Верно')
        break
    else:
        print('Неверно')
