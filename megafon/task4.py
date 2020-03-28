number_string = input("Enter the number:")
number_length = len(number_string)
print(number_length)
current_number = 0
max_digit = 0

while current_number < number_length:
    current_digit = int(number_string[current_number])
    if max_digit < current_digit:
        max_digit = current_digit
    current_number = current_number + 1

print(max_digit)
