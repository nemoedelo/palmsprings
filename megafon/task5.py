from functools import reduce

"""
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
"""


def multiply(first, second):
    return first * second


result = reduce(multiply, range(100, 1001))
print(result)
