import numpy as np
import matplotlib.pyplot as plt
import csv

with open('D:/Coding/Python/FundDataSci/Titanic_data.csv') as file:
    reader = csv.reader(file)
    agesLived = []
    agesDied = []
    for column in reader:
        if (column[0] == '1'):
            agesLived.append(column[3])
        else:
            agesDied.append(column[3])
    agesDied.pop(0)
    agesLived = list(map(float, agesLived))
    agesDied = list(map(float, agesDied))
        
pos = [1.5, 2.5]
data = [agesLived, agesDied]

plt.violinplot(data, pos, points=100, widths=0.75, showextrema=True, showmedians=True)

plt.title('Titanic Passenger Ages')
plt.xlabel('Survived                                                 Died')
plt.ylabel('Passenger Age')
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])

plt.show()
