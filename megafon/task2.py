initial_list = [1, 3, 5, 1, 4, 2, 19]

"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""


def check_values(values):
    i = 0
    while i < len(values):
        if i == 0:
            yield values[i]
            i += 1
        else:
            if values[i] > values[i - 1]:
                yield values[i]
                i += 1
            else:
                i += 1
                continue


gen = check_values(initial_list)

result = [n for n in gen]
print(result)
