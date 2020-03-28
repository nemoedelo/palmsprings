profit = int(input("Enter your profit:"))
loss = int(input("Enter your loss:"))

pnl = profit - loss
if pnl > 0:
    print("WoW! You've made a profit. Now it's time to pay taxes!")
else:
    print("Time to close the business.")
    exit(0)

marginal_profitability = pnl / profit
print("Profitability:", marginal_profitability)

empoyees_quantity = int(input("How much employees do you have?"))
profit_per_employee = profit / empoyees_quantity
print("Your profit per employee is:", profit_per_employee)
