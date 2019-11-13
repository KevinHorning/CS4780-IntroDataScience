import numpy as np
import matplotlib.pyplot as plt
import csv

with open('D:/Coding/Python/FundDataSci/Titanic_data.csv') as file:
    reader = csv.reader(file)
    survivedAndMale = 0
    survivedAndFemale = 0
    diedAndMale = 0
    diedAndFemale = 0
    for column in reader:
        if (column[0] == '1' and column[2] == '0'):
            survivedAndMale += 1
        if (column[0] == '1' and column[2] == '1'):
            survivedAndFemale += 1
        if (column[0] == '0' and column[2] == '0'):
            diedAndMale += 1
        if (column[0] == '0' and column[2] == '1'):
            diedAndFemale += 1
 
plt.scatter([0, 0, 1, 1], [0, 1, 0, 1], s = [diedAndMale, diedAndFemale, survivedAndMale, survivedAndFemale])
plt.title('Titanic Survival and Gender')
plt.ylabel('Gender')
plt.xlabel('Survival')

plt.set_xticks(1)

plt.show()
