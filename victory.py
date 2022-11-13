""" Module 6"""

question1 = 'Введите год рождения Исаака Ньютона: '  # 1643
answer_to_question1 = 1643
question2 = 'Введите год рождения Билла Гейста: '  # 1955
answer_to_question2 = 1955
question3 = 'Введите год рождения Альберта Энштейна: '  # 1879
answer_to_question3 = 1879
question4 = 'Введите год рождения Николы Тесла: '  # 1856
answer_to_question4 = 1856
question5 = 'Введите год рождения Томаса Эдисона: '  # 1847
answer_to_question5 = 1847

while True:
    count_questions = 5
    count_correct_answer = 0
    answer1 = int(input(question1))
    if answer1 == answer_to_question1:
        count_correct_answer += 1

    answer2 = int(input(question2))
    if answer2 == answer_to_question2:
        count_correct_answer += 1

    answer3 = int(input(question3))
    if answer3 == answer_to_question3:
        count_correct_answer += 1

    answer4 = int(input(question4))
    if answer4 == answer_to_question4:
        count_correct_answer += 1

    answer5 = int(input(question5))
    if answer5 == answer_to_question5:
        count_correct_answer += 1

    print('Количество правильных ответов:', count_correct_answer)
    print('Количество ошибок:', count_questions - count_correct_answer)
    percent_correct_answer = count_correct_answer * 100 / count_questions
    print('Процент правильных ответов:', percent_correct_answer)
    print('Процент неправильных ответов:', 100 - percent_correct_answer)

    repeat = input('Начать игру сначала? (Для повтора игры введите - Y, для окончания игры - любой другой символ): ')
    if repeat != 'Y' and repeat != 'y':
        break
