with open("resources/task3.txt", mode="r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Lines quantity:", len(lines))
    dict = {}
    for l in lines:
        splitted = l.split()
        dict[splitted[0]] = splitted[1]

    filtered = (n for n in dict if int(dict[n]) > 20000)
    print(list(filtered))
