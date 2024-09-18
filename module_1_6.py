# Создать переменную my_dict и присвоить переменной словарь из нескольких пар ключ-значение.
my_dict = {'Леонид': 1961, 'Надя': 1960, 'Коля': 1968}
# Выведим словарь на экран
print(my_dict)
# Выведим значения словаря по ключу
print(my_dict['Коля'])
# необходимо добавить пару ключ -> значение
my_dict['Александра'] = 2004
# Теперь
print(my_dict['Александра'])
# прежде чем выводить значение по не существующиму ключу необходимо добавить пару в словарь
# Словарь таким образом сейчас имеет вид
print(my_dict)
# Добавить несколько пар новых значений в словарь можно командой update. Формат команды следуюший
my_dict.update({'Валя': 2006, 'Витя': 2010})
# Результат выведим
print(my_dict)
# Для удаления по ключу осуществлятся командой del формат команды del my_dict['Леонид']
# НО нам по условию необходимо вывести значение удаленной пары для этого используют команду pop()
print(my_dict.pop('Леонид'))
# Выведено значение соответсвующее удаленному ключу. Посмотрим на измененный словарь
print(my_dict)
# Как видим ключ 'Леонид' и его значение удалено но перед этим мы ввели его на экран.
# Также мы можем сохранить это значение в какой либо переменной
# Теперь содадим множество из разных типов данных
my_set = {1, 2, 2, 3, 3, 4, 3, 'Python', (1, 2, 3)}
# На вывод
print(my_set)
# Как видим повторяюшиеся значения в создаваемом множестве удаляютя так как множество это коллекция УНИКАЛЬНЫХ значений
# Существует возможность преобразование списка во множество. Создадим список
my_list = [1, 1, 2, 2, 2, 3, 3, 4]
my_set_1 = set(my_list)
# Выведим на экран
print(my_set_1)
# Как видим сформировалось множество из уникальных значений. То есть повторяющиеся значения не вошли во множество
# Для добавления элементов во множество используют команду add
my_set.add('Java')
my_set.add('C#')
print(my_set)
# Как видим во множество добавилось два новых элемента 'Java' и 'C#'
# Для удаления элементов из множесвта используют две команды 'discard' и 'remove'.
# Команда 'discard' нес ообщает об ошибке при попытке удалить не существующее значение.
# Поэтому предпочтительнее использовать команду 'remove'
my_set.remove('Python')
# Посмотрим на измененное множество
print(my_set)
# Как видим элемент 'Python' удален из множества