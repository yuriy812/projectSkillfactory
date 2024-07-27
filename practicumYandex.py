n = int(input('Введите количество дел на сегодня: '))
todo = []

print('Введите задачи на сегодня: ')
for i in range(n):
    task = input(f'{i + 1}) ')
    todo.append(task)

print('Список дел на сегодня:')
print(todo)

n = int(input('Введите номер дела, которое нужно отредактировать: '))
task = input('Введите новое описание для дела: ')
todo[n - 1] = task

n = int(input('Введите индекс дела, которое нужно удалить: '))
todo.pop(n)

print('Список дел на сегодня:')
print(todo)
