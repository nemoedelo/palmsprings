language = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("resources/task4.txt", mode="r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Lines quantity:", len(lines))
    dict = {}
    for l in lines:
        splitted = l.split()
        dict[splitted[0]] = splitted[2]

with open("resources/task4ru.txt", mode="w", encoding="utf-8") as f:
    for s in dict:
        f.write(language[s])
        f.write(" - ")
        f.write(dict[s])
        f.write("\n")
