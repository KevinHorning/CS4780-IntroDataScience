import numpy as np
import matplotlib.pyplot as plt
import random

def getStDev(ratios):
    mean = sum(ratios) / len(ratios)
    squares = []
    for ratio in ratios:
        squares.append((ratio - mean)**2)

    return sum(squares) / len(ratios)

x = np.zeros((4, 100))
ratios = []

for index in range(100):
    x[0, index] = random.gauss(165, 25)
    x[1, index] = random.gauss(200, 50)
    ratios.append(x[1, index] / x[0, index])

stDev = getStDev(ratios)
for index in range(100):
    x[2, index] = ratios[index] + random.gauss(0, stDev)    

r = 1.8

for index in range(100):
    if (x[2, index] > r):
        x[3, index] = 1
    else:
        x[3, index] = 0

plt.title('Height vs Weight')
plt.ylabel('Weight(pounds)')
plt.xlabel('Height(cm)')
plt.scatter(x[[0], :], x[[1], :], c = x[[3], :])

'''
glucoses = []
for index in range(100):
    glucoses.append(x[2, index])

fig, axs = plt.subplots()
plt.title('Glucose Levels')
plt.ylabel('Glucose')    
axs.boxplot(glucoses)

plt.title('Height vs Weight')
plt.ylabel('Weight(pounds)')
plt.xlabel('Height(cm)')
plt.scatter(x[[0], :], x[[1], :])

x = np.random.normal(size = 1000)
plt.hist(x, normed=True, bins=30)
plt.ylabel('Probability');
plt.show()
'''