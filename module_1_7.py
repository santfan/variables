# Имеем входные данные
# Список оценок студентов
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество студентов
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Так как множества являются не упорядоченным преобразуем тип множество в тип список
# Так как список оценок представлен в алфавитном порядке отсортируем список стендтов командой sorted()
stud_list = sorted(list(students))
# Посмотрим результат
print(stud_list)

['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']

# Создадим пустой словарь
stud_dict = {}
# Заполним пустой словарь
stud_dict.update({stud_list[0]: sum(grades[0]) / len(grades[0]),
                  stud_list[1]: sum(grades[1]) / len(grades[1]),
                  stud_list[2]: sum(grades[2]) / len(grades[2]),
                  stud_list[3]: sum(grades[3]) / len(grades[3]),
                  stud_list[4]: sum(grades[4]) / len(grades[4])})

# Выведим результат
print(stud_dict)

{'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}