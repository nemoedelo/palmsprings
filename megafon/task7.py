import json
from statistics import mean

with open("resources/task7.txt", mode="r", encoding="utf-8") as f:
    firms = {}
    for line in f.readlines():
        splitted = line.split()
        name = splitted[0]
        revenue = int(splitted[2])
        costs = int(splitted[3])
        profit = revenue - costs
        firms[name] = profit

positive_profits = (n for n in firms.values() if n > 0)
average_profit = mean(positive_profits)
result = [firms, {"Average profit": average_profit}]
print(json.dumps(result))
