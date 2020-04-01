input_str = input("The long sentence ")
string_array = input_str.split()
i = 1
for s in string_array:
    if len(s) >= 10:
        s = s[0:9]
    print(f"{i}: {s}")
    i = i + 1
