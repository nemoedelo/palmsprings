import re


def getNumbers(str):
    array = re.findall(r'[0-9]+', str)
    array = [int(i) for i in array]
    return array


with open("resources/task6.txt", mode="r", encoding="utf-8") as f:
    dict = {}
    for line in f.readlines():
        subject = line.split()[0]
        subject = subject[0:len(subject) - 1]
        numbers = getNumbers(line)
        print(subject, sum(numbers))
        dict[subject] = sum(numbers)

    print(dict)
