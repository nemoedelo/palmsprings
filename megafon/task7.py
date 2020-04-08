"""Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!."""


def factorial(my_number):
    current_factorial = 1

    for n in range(1, my_number + 1):
        current_factorial = current_factorial * n
        yield current_factorial


def print_factorials(input):
    factorial_generator = factorial(input)
    i = 1
    for n in factorial_generator:
        print(f"{i}!={n}")
        i += 1


print_factorials(5)
