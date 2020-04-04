"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def divide(base, divider):
    if divider == 0:
        raise ValueError("Divider shouldn't be 0")
    return base / divider


first = int(input("Enter first value:"))
second = int(input("Enter divider value:"))

print(divide(first, second))
