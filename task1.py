# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_list = [30, 1, 22, 34, 1, 1, 4, 27, 77, 1, 78, 13, 55]
print([j for i, j in enumerate(my_list) if i != 0 and j > my_list[i - 1]])



