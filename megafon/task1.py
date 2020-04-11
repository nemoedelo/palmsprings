with open("resources/task1.txt", "w") as f:
    inputstr = "blank"
    while inputstr != "":
        inputstr = input("Введите строку:")
        f.write(inputstr)
        f.write("\n")
