"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""


def my_pow(base, power):
    validate_args(base, power)
    result = 1
    for _ in range(power, 0):
        result = result / base
    return result


def validate_args(base, power):
    if base < 1:
        raise ValueError("Base should be positive")
    if power >= 0:
        raise ValueError("Power should be negative")


print(my_pow(5, -3))
