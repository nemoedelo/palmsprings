input_str = input("The long sentence ")
string_array = input_str.split()

array_elements_count = len(string_array)
i = 0
while i < array_elements_count:
    if (i % 2 == 1):
        first_element = string_array[i]
        second_element = string_array[i - 1]
        string_array[i] = second_element
        string_array[i - 1] = first_element
    i = i + 1

print(string_array)
