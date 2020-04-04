"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
 разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
 Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func()."""


def my_capitalize(word):
    return str(word).capitalize()


def multiword_capitalize(text):
    word_array = text.split()
    result = ""
    for word in word_array:
        result = result + my_capitalize(word) + " "
    return trim_last_space(result)


def trim_last_space(result):
    return result[0:len(result) - 1]


my_text = input("Please enter the text:")

print(multiword_capitalize(my_text))
