f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices = listItems
for i in range(0, len(listItems)):
    appleprices[i] = float(listItems[i])

current_max_val = 0
potential_profit = 0
max_profit_val = 0

for price in reversed(appleprices):
    current_max_val = max(current_max_val, price)
    potential_profit = current_max_val - price
    max_profit_val = max(potential_profit, max_profit_val)

print(current_max_val)
print(potential_profit)
print(max_profit_val)