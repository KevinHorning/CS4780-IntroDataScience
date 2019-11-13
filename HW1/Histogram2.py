import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
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

n_groups = 2

means_men = (survivedAndMale, diedAndMale)

means_women = (survivedAndFemale, diedAndFemale)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.5

rects1 = ax.bar(index, means_men, bar_width, color='b', label='Men')

rects2 = ax.bar(index + bar_width, means_women, bar_width, color='r', label='Women')

ax.set_ylabel('Frecuency')
ax.set_title('Titanic Survival and Gender')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Survived', 'Died'))
ax.legend()

fig.tight_layout()
plt.show()
