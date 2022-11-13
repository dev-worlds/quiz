""" Module 5"""

age = 1799
day = 6
answer_age = None
answer_day = None

while answer_age != age:
    answer_age = int(input('Введите год рождения А.С Пушкина: '))
    if age == answer_age:
        while answer_day != day:
            answer_day = int(input('Введите день рождения А.С Пушкина: '))
            if answer_day == day:
                print('Верно')
            else:
                print('Неверный день рождения')
    else:
        print('Неверный год рождения')
