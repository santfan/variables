# Создадим кортежи разными способами
immutable = 1, 2, 57, 'Leonid', ['python', 'java']
immutable_1 = (1, 2, 57, 'Leonid', ['python', 'java'])

# Преобразование
num = ['раз', 2]
immutable_2 = tuple(num)

# Выведем на экран
print(immutable, type(immutable))
print(immutable_1, type(immutable_1))
print(immutable_2, type(immutable_2))

# Попробуем изменить элемент кортежа
# Обратимся к элементу кортежа с индеком 2 и изменим его
#immutable[2] = 300  # было значение 57 Эта часть кода не работает
# выведем изменный кортеж
#print(immutable)
# Ошибка типа TypeError: 'tuple' object does not support item assignment

# Кортеж изменять в общем случае нельзя
# но если элемент кортежа сам по себе изменяем то
# например элемент с индесом 4 сам по себе список - изменяем. Попробуем
immutable[4][1] = 'Cи' # Было 'Java'
# Вывод на экран
print(immutable)
# Зменения произошли

# Теперь со списком создадим
mutable = ['три', 5, 24]

# Преобразование
string = 'три', 5, 24
mutable_1 = list(string)

# Вывод на экран
print(mutable, type(mutable))
print(mutable_1, type(mutable_1))

# изменения списков возможна
mutable[2] = 17 # Было 24
# Вывод на экран
print(mutable, type(mutable))