"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов."""


def max(first, second, third):
    args_array = [first, second, third]
    args_array.sort()
    return args_array[1] + args_array[2]


print(max(3, 2, 5))
