current_value = int(input("Your current value:"))
target_value = int(input("Your target value:"))
day_count = 1  # We start counting days from 1 as the God did
if target_value < 0 or current_value < 0:
    print("Value can't be negative!")
    exit(1)

while current_value < target_value:
    current_value = current_value * 1.1
    day_count = day_count + 1

print(day_count)
