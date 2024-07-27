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
        marks = [random.randint(1,5) for i in range(3)]  # generate a list of 3 random marks
        students_marks[student][class_] = marks
# Print the dictionary of student marks
for student in students:
    print(f'''{student}
    {students_marks[student]}''')
