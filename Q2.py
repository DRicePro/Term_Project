import numpy as np
import matplotlib.pyplot as plt

f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices = listItems
for i in range(0, len(listItems)):
    appleprices[i] = float(listItems[i])

x = np.linspace(1, 252, len(appleprices))
y = appleprices
plt.plot(x, y)
plt.xlabel("Day")
plt.ylabel("Trading Price")
plt.title("Apple Stock Price, Nov 2019 to Nov 2020")
plt.show()