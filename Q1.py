import numpy as np

f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices = listItems
for i in range(0, len(listItems)):
    appleprices[i] = float(listItems[i])
    print(appleprices[i])

mean_apple = np.mean(appleprices)
std_apple = np.std(appleprices)

print(mean_apple)
print(std_apple)