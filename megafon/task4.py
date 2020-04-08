"""
Представлен список чисел.
 Определить элементы списка, не имеющие повторений.
 Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
"""

initial_list = [1, 3, 5, 1, 4, 2, 19]


def count(param, values):
    i = 0
    for n in values:
        if n == param:
            i += 1
    return i


def check_values(values):
    i = 0
    while i < len(values):
        if count(values[i], values) == 1:
            yield values[i]
            i += 1
        else:
            i += 1
            continue


gen = check_values(initial_list)

result = [n for n in gen]
print(result)
