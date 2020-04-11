f = open("resources/task2.txt", mode="r", encoding="utf-8")
lines = f.readlines()
print("Lines quantity:", len(lines))
for l in lines:
    print("Words quantity:", len(l.split()))
