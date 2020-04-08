from itertools import cycle, count

"""
Реализовать два небольших скрипта: 
а) итератор, генерирующий целые числа, начиная с указанного, 
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""


def infinite_collection():
    global n
    input = [1, 3, 5, 7]
    input_cycle = cycle(input)
    for n in input_cycle:
        print(n)


infinite_collection()


def increment_count():
    global n
    my_start = 5
    incrementor = count(my_start)
    for n in incrementor:
        print(n)


increment_count()
