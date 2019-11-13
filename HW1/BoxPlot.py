import numpy as np
import matplotlib.pyplot as plt
import csv

with open('D:/Coding/Python/FundDataSci/HW1/titanic_data.csv') as file:
    reader = csv.reader(file)
    agesLived = []
    agesDied = []
    for column in reader:
        if (column[0] == '1'):
            agesLived.append(column[6])
        else:
            agesDied.append(column[6])
    agesDied.pop(0)
    agesLived = list(map(float, agesLived))
    agesDied = list(map(float, agesDied))

data = [agesLived, agesDied]

fig, ax = plt.subplots()
ax.boxplot(data)
plt.title('Titanic Passenger Fares')
plt.ylabel('Ticket Price')

plt.show()
