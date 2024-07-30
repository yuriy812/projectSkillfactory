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
    elif command == 7:
        # Выводим существующие предметы
        print('Предметы, которые уже существуют:')
        for i in classes:
            print(f'-- {i}')
        # Запрашиваем у пользователя ввод нового предмета
        new_class = input('Введите название нового предмета: ')
        # Проверяем, существует ли уже этот предмет
        if new_class in classes:
            print(f'ОШИБКА: Предмет "{new_class}" уже существует.')
        else:
            # Добавляем предмет в список классов
            classes.append(new_class)

            # Обновляем оценочные записи для каждого ученика, добавляя пустой список оценок для нового предмета
            for student in students_marks:
                students_marks[student][new_class] = []  # Инициализируем пустой список оценок для нового предмета
                print(f'Предмет "{new_class}" успешно добавлен.')

                # Вывод обновленного списка предметов для всех учеников
                print('Обновленный список оценок для всех учеников:')
            for student in students_marks:
                print(f'{student}: {students_marks[student]}')
    elif command == 8:
        print("Удаление предмета")
        for i in classes:
            print(f'-- {i}')
        # Запрашиваем у пользователя ввод удаления предмета
        removal_class = input('Введите название удаляемого предмета: ')
        if removal_class not in classes:
            print(f'ОШИБКА: Предмет "{removal_class}" не найден в списке.')
        else:
            classes.remove(removal_class)
            print(f'Предмет "{removal_class}" был успешно удален.')
            print()
            for n in classes:
                print(f'Список предметов теперь: {n}')

    elif command == 9:
        print('Информация по ученикам с плохой успеваемостью')
        # Порог для плохой успеваемости
        threshold = 3.0
        # Список учеников с хорошей успеваемостью
        students_with_good_performance = {}
        # Вычисляем средний балл для каждого ученика
        for student, subjects in students_marks.items():
            total_grades = []

            # Собираем все оценки
            for subject, grades in subjects.items():
                if all(isinstance(grade, (int, float)) for grade in grades):
                    total_grades.extend(grades)

            # Вычисляем средний балл, если есть оценки
            if total_grades:
                average = sum(total_grades) / len(total_grades)
                if average < threshold:
                    students_with_good_performance[student] = average
            else:
                print(f"Нет оценок для ученика {student}.")

        # Вывод информации по ученикам с плохой успеваемостью
        if students_with_good_performance:
            print("Ученики с хорошей успеваемостью:")
            for student, average in students_with_good_performance.items():
                print(f'{student}: Средний балл {average:.2f}')
        else:
            print("Нет учеников с плохой успеваемостью.")

    elif command == 10:
        print('Информация по ученикам с хорошей успеваемостью')
        # Порог для плохой успеваемости
        threshold = 3.0
        # Список учеников с хорошей успеваемостью
        students_with_good_performance = {}
        # Вычисляем средний балл для каждого ученика
        for student, subjects in students_marks.items():
            total_grades = []

            # Собираем все оценки
            for subject, grades in subjects.items():
                if all(isinstance(grade, (int, float)) for grade in grades):
                    total_grades.extend(grades)

                    # Вычисляем средний балл, если есть оценки
            if total_grades:
                average = sum(total_grades) / len(total_grades)
                if average >= threshold:
                    students_with_good_performance[student] = average
            else:
                print(f"Нет оценок для ученика {student}.")

                # Вывод информации по ученикам с хорошей успеваемостью
        if students_with_good_performance:
            print("Ученики с хорошей успеваемостью:")
            for student, average in students_with_good_performance.items():
                print(f'{student}: Средний балл {average:.2f}')
        else:
            print("Нет учеников с хорошей успеваемостью.")
    elif command == 11:
        print('11. Выход из программы')
        break

    else:
        print('ОШИБКА: неправильная команда. Попробуйте еще раз.')
