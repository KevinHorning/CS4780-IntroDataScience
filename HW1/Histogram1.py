import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import csv

with open('D:/Coding/Python/FundDataSci/Titanic_data.csv') as file:
    reader = csv.reader(file)
    ages = []
    for column in reader:
        ages.append(column[3])
    ages.pop(0)
    ages = list(map(float, ages))
    
data = ages
n, bins = np.histogram(data, 80)

left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n
nrects = len(left)

nverts = nrects * (1 + 3 + 1)
verts = np.zeros((nverts, 2))
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5, 0] = left
verts[0::5, 1] = bottom
verts[1::5, 0] = left
verts[1::5, 1] = top
verts[2::5, 0] = right
verts[2::5, 1] = top
verts[3::5, 0] = right
verts[3::5, 1] = bottom

fig, ax = plt.subplots()
barpath = path.Path(verts, codes)
patch = patches.PathPatch(barpath, facecolor='green', edgecolor='blue', alpha=2)
ax.add_patch(patch)

ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())
plt.title('Titanic Passenger Ages (80 Bins)')
plt.xlabel('Passenger Age')
plt.ylabel('Frequency')

plt.show()
