list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_number = list_numbers[max_index]

for i, current_number in enumerate(list_numbers):  # перебираем пары индекс - значение
    max_number = list_numbers[max_index]
    if current_number >= max_number:  # если текущей номер больше или равен тому, который встречали ранее
        max_index = i  # то перезаписываем индекс максимального номера
        max_number = list_numbers[max_index]  # и перезаписываем номер

list_numbers[max_index], list_numbers[len(list_numbers)-1] = list_numbers[len(list_numbers)-1], list_numbers[max_index]

print(list_numbers)
