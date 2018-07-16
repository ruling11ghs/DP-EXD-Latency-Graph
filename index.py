from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import datetime
import calendar
import matplotlib.patches as mpatches
from string import digits

titleConst = ['TS', 'HR', 'BR', 'PS', 'ASV', 'AXF', 'ACO', 'ACO2', 'AXF2', 'ACV', 'ACO3', 'AXF3', 'ACL', 'AXF4', 'ARE', 'ACO4', 'PC', 'CS', 'HS',
              'BS', 'HR2', 'BR2', 'PS2', 'ASV2', 'AXF5', 'PS3', 'AOE', 'ACO5', 'AOE2', 'ACO6', 'AXF6', 'ARE2', 'PC2','ACL2', 'ACO7', 'AXF7', 'PC3', 'HS2', 'BS2', 'TC']
titleFilter = [] # put in here what you want the graph to show in the same format of titleConst
                 # this is not required
if len(titleFilter) == 0:
    titleFilter = titleConst

data = []
file_object = open(r"C:\Users\IBM_ADMIN\Documents\Python\extLatencyLog.txt") # here you can change the string to r"(location of file)" for the required file
fileList = file_object.readlines()
filter = "" # if you want a filter, put either the full URL or a section of what you are looking for
               # this is not required

if len(filter) == 0:
    for i in range(len(fileList)):
        file = fileList[i]
        data.append(file)
else:
    for i in range(len(fileList)):
        if filter in fileList[i]:
            file = fileList[i]
            data.append(file)

xAxis = []
yAxis = []
zAxis = []
yLabels = []
xLabels = []
date = ""
zAxis2 = []

for i in range(len(data)):
    use = ""
    for m in range(len(data)):
        if i == m:
            date1 = str(data[i])[0:24] # this should be the range for the number of characters for the date and time of the entry
            use = data[i]
            date = datetime.strptime(date1, '%a %b %d %Y %H:%M:%S') # the time should be in the '...' order e.g: Tues Jul 03 2018 17:30:25
    unixDate = calendar.timegm(date.utctimetuple())
    xLabels.append(unixDate)

    step1 = use.split("ExtLatency: ")[1] #ExtLatency needs to be the word/phrase that is directly before the stages and times
    step2 = step1.split(" ")[0:3]
    step3 = "".join(step2)
    step4 = step3.split("=")
    step5 = "".join(step4)
    step6 = step5.split(",")
    test = str(step6[0])

    array = []
    word = ""
    number = ""

    for i in range(len(step6)):
        test = str(step6[i])
        for i in range(len(test)):
            if ord(test[i]) <= ord("Z") and ord(test[i]) >= ord("A"):
                word = word[:(i)] + test[i] + word[(i):]
            else:
                number = number[:(i - 1)] + test[i] + number[(i - 1):]
        array.append(word)
        array.append(number)
        word = ""
        number = ""

    array.pop() # this removes the last value from the array array
    array.pop() # you may not need these or may need more/less of these
    number2 = []
    x = []
    y = [0]
    z = []
    zTemp = []
    zCnt = 0

    for i in range(len(array)):
        if i % 2 == 1:
            number2.append(int(array[i]))
        else:
            zCnt = zCnt + 1
            z.append(array[i])
            zTemp.append(zCnt)

    for i in range(len(number2) - 1):
        i += 1
        n = int(number2[i]) - int(number2[i - 1])
        y.append(n + 0.001)

    counter = 0
    titleCount = 0
    while (counter < len(z)):
        tempv = titleConst[titleCount].translate(
            {ord(k): None for k in digits})
        if (z[counter] == tempv):
            z[counter] = titleConst[titleCount]
            counter += 1
            titleCount += 1
        else:
            titleCount += 1


    for i in range(len(data)):
        if len(zAxis) == i:
            for j in range(len(y)):
                x.append(i + 1)

    if i == 0:
        xAxis = [x]
        yAxis = [y]
        zAxis = [zTemp]
        yLabels = [z]
    else:
        xAxis.append(x)
        yAxis.append(y)
        zAxis.append(zTemp)
        yLabels.append(z)
biggest = yLabels[0]
for i in range(len(yLabels)):
    if len(biggest) < len(yLabels[i]):
        biggest = yLabels[i]

title = {}
for i in range(len(titleConst)):
    title[titleConst[i]] = i + 1

yAxis2 = []
xAxis2 = []
yAxis22 = []
for i in range(len(data)):
    yAxis2.append([])
    yAxis22.append([])
    xAxis2.append([])
    for tc in range(len(titleFilter)):
        for yl in range(len(yLabels[i])):
            if (yLabels[i][yl] == titleFilter[tc]):
                yAxis2[i].append(title[titleFilter[tc]])
                yAxis22[i].append(yAxis[i][yl])

                xAxis2[i].append(xAxis[i][yl])
        if (title[titleFilter[tc]] not in yAxis2[i]):

            yAxis2[i].append(title[titleFilter[tc]])
            yAxis22[i].append(0)
            xAxis2[i].append(xAxis[i][0])


xLabels2 = []
divide = 6   # this should be the number of labels on the x axis that show up for your number of entries
tempNumber = len(data) // divide
tempNumber2 = 0
for i in range(1,divide):
    tempNumber2 = tempNumber * i
    xLabels2.append(xLabels[tempNumber2])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.xlim(1, len(data))

colours = ['k', 'r', 'm', 'b', 'c', 'g', 'y'] # this should be the colours that you want to see for the legend (key). it can be any length
index = 0
legendLabels = []
addon2 = plt.Rectangle((0, 0), 2, 1, fc=colours[index])

for i in range(len(titleFilter)):
    addon2 = plt.Rectangle((0, 0), 2, 1, fc=colours[index])
    index += 1
    if index > len(colours) - 1:
        index = 0
    legendLabels.append(addon2)

colours2 = ['k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g',

            'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y']


for i in range(len(data)):
    ax.bar(xAxis2[i], yAxis22[i], yAxis2[i], zdir='y',color=colours2, edgecolor=colours2, alpha=0.5, width=1)

figsize = (len(data), len(biggest))

ax.legend(legendLabels, titleFilter)

ax.w_yaxis.set_ticklabels("")
ax.w_xaxis.set_ticklabels(xLabels2)
ax.set_xlabel('Timestamp')
ax.set_ylabel('Stage')
ax.set_zlabel('value')
plt.show()

fig.savefig('graph.png') # you can change the name of where to save the file to whatever you want

# I have tested the code with many different entries. The max I tried that worked was 10000. I would not recommend this. You should do about 100 entries to test as it is quick.
# You will have to make the text with 100 entries in. This just runs for however many entries you have made.
