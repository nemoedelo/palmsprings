"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""

accumulated_sum = 0
while True:
    input_str = input("Input numbers with spaces: or B to break")
    if input_str == "B":
        print("Program end. Accumulated value:", accumulated_sum)
        break
    str_array = input_str.split()
    for num in str_array:
        accumulated_sum = accumulated_sum + int(num)
    print(accumulated_sum)
