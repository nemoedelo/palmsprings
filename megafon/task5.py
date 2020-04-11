with open("resources/task5.txt", mode="w", encoding="utf-8") as f:
    for s in range(0, 100):
        f.write(str(s))
        f.write(" ")
        f.flush()

with open("resources/task5.txt", mode="r", encoding="utf-8") as f:
    aggregate = 0
    for number in f.readline().split():
        aggregate = aggregate + int(number)

    print(aggregate)
