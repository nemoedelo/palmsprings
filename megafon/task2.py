input_number = int(input("Enter the seconds quantity:"))
if input_number > 60 * 60 * 24:
    print("Validation error: the value is too big " + str(input_number))
    exit(1)

seconds = input_number % 60
minutes = input_number // 60
hours = minutes // 60
minutes_to_print = minutes - (hours * 60)
print(f"{hours}:{minutes_to_print}:{seconds}")
