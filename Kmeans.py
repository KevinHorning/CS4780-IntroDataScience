# k means algorithm 
# can input any 2 dimensional numerical data into data variable, and any int for k (will need to modify size of colors list for visualization)

import random, math;
import matplotlib.pyplot as plt

data = [(0,7), (1,1), (1,6), (1,8), (2,5), (2,8), (3,0), (3,6), (3,7), (5,3), (6,2), (6,4), (7,2), (7,3), (7,5), (7,8), (8,3), (8,4), (9,9)]
k = 4;

# initializes k random centers
centers = []
pickedIndices = []
while (len(centers) < k):
    ranIndex = random.randint(0,len(data) - 1)
    if (ranIndex not in pickedIndices):
        pickedIndices.append(ranIndex)
        centers.append(data[ranIndex]) 
        
labels = []
labelsChange = True
iii = 0
while (labelsChange):
    # reevaluate centers
    if (len(labels) != 0):
        for centerIndex in range(k):
            # get this center's data points
            centerPoints = []
            for labelIndex in range(len(labels)):
                if (labels[labelIndex] == centerIndex):
                    centerPoints.append(data[labelIndex])
            
            # averages points values to set new center
            Xsum = 0.0
            Ysum = 0.0
            for i in centerPoints:
                Xsum += i[0]
                Ysum += i[1]
            Xaverage = Xsum / len(centerPoints)
            Yaverage = Ysum / len(centerPoints)
            centers[centerIndex] = (Xaverage, Yaverage)
    
    # assign labels to closest center for each point
    newLabels = []
    for i in data:
        distancesToCenters = []
        for j in centers:
            distancesToCenters.append(math.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2))                    
        newLabels.append(distancesToCenters.index(min(distancesToCenters)))
    
     # determine if centers change
    if (len(labels) == 0):
        labels = newLabels
    elif (labels == newLabels):
        labelsChange = False
    else:
        labels = newLabels
    
    # visualization
    colors = ['red', 'blue', 'yellow', 'green']    
    for i in centers:
        plt.scatter(i[0], i[1], s = 150 ,color = colors[centers.index(i)])
    for i in data:
        plt.scatter(i[0], i[1], color = colors[labels[data.index(i)]])    
    plt.show()
        