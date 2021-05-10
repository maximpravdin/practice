# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного. Для генерации число Enter,',
      'Для выхода нажмите - "q"')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повторяет элементы списка. Для генерации следующего повторения нажмите Enter,',
      'Для выхода - "q"')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()