import random

# List of students
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# Sort the list of students
students.sort()
# List of subjects
classes = ['Математика', 'Русский язык', 'Информатика']
# Empty dictionary to store student marks
students_marks = {}
# Generate random marks for each student and subject combination
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]  # Generate a list of 3 random marks
        students_marks[student][class_] = marks

    # Print the dictionary of student marks
for student in students:
    print(f'''{student}  
    {students_marks[student]}''')
print()
print('''Список команд:  
        1. Добавить оценку ученика по предмету  
        2. Вывести средний балл по всем предметам по каждому ученику  
        3. Вывести все оценки по всем ученикам  
        4. Удалить оценку у ученика по предмету  
        5. Информации по всем оценкам для определенного ученика
        6. Средний балла по каждому предмету по определенному ученику 
        7. Добавление предмета
        8. Удаление предмета
        9. Информация по ученикам с плохой успеваемостью
        10. Информация по ученикам с хорошей успеваемостью  
        11. Выход из программы''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))

        if student in students_marks and class_ in students_marks[student]:
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum / marks_count:.2f}')
            print()

    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        print('4. Удалить оценку у ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')

        if student in students_marks and class_ in students_marks[student]:
            print(f'Оценки для {student} по предмету {class_}: {students_marks[student][class_]}')
            try:
                mark = int(input('Введите оценку для удаления: '))
                if mark in students_marks[student][class_]:
                    students_marks[student][class_].remove(mark)
                    print(f'Для {student} по предмету {class_} удалена оценка {mark}')
                    print(f'Оценки для {student} по предмету {class_}: {students_marks[student][class_]}')
                else:
                    print(f'ОШИБКА: У {student} по предмету {class_} нет такой оценки {mark}')
            except ValueError:
                print('ОШИБКА: Введите корректное числовое значение.')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 5:
        print('5. Информация по всем оценкам для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Информация по всем оценкам {student} по предметам:')
            for class_ in classes:
                if class_ in students_marks[student]:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                else:
                    print(f'\t{class_} - Оценок нет')
        else:
            print('ОШИБКА: Ученик не найден.')
    # Новый пункт для вывода среднего балла по предмету для ученика
    elif command == 6:
        print('6. Средний балл по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')

        if student in students_marks:
            print(f'Средний балл для {student}:')
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum / marks_count:.2f}')
        else:
            print('ОШИБКА: Вероятно, такого ученика не существует.')

    elif command == 11:
        print('11. Выход из программы')
        break

    else:
        print('ОШИБКА: неправильная команда. Попробуйте еще раз.')
