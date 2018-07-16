from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import datetime
import calendar
import matplotlib.patches as mpatches
from string import digits

titleConst = ['TS', 'HR', 'BR', 'PS', 'ASV', 'AXF', 'ACO', 'ACO2', 'AXF2', 'ACV', 'ACO3', 'AXF3', 'ACL', 'AXF4', 'ARE', 'ACO4', 'PC', 'CS', 'BS', 'HS',
              'BS', 'HR2', 'BR2', 'PS2', 'ASV2', 'AXF5', 'PS3', 'AOE', 'ACO5', 'AOE2', 'ACO6', 'AXF6', 'ARE2', 'PC2','ACL2', 'ACO7', 'AXF7', 'PC3', 'HS2', 'BS2', 'TC']
#data1 = "Tue Jul 03 2018 17:41:02 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi): tid(2681233)[172.18.8.14] gtid(c0873c625b3b990d0028e991): ExtLatency: TS=0,HR=0,BR=0,PS=0,ASV=0,AXF=1,ACO=1,ACO=1,AXF=3,ACO=3,AXF=8,ACL=37,AXF=37,ARE=37,ACO=37,PC=37,CS=37,HS=37,BS=37, == HR=38,BR=38,PS=38,ASV=38,AXF=38,AOE=38,ACO=38,AOE=38,ACO=38,AXF=39,ARE=39,ACO=39,AXF=39,PC=39,HS=39,BS=39,TC=39, [https://172.18.13.22:443/perf/private/v1/shopping_lists/me]"
#data2 = "Tue Jul 03 2018 17:30:25 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi): tid(2593889)[172.18.6.14] gtid(c0873c625b3b969000279461): ExtLatency: TS=0,HR=0,BR=0,PS=0,ASV=0,AXF=1,ACO=1,ACO=1,AXF=4,ACV=4,ACO=4,AXF=10,ACL=56,AXF=56,ARE=56,ACO=56,PC=57,CS=57,HS=57,BS=57, == HR=57,BR=57,PS=57,ASV=57,AXF=58,AOE=58,ACO=58,AOE=58,ACO=58,AXF=58,ARE=59,ACO=59,AXF=59,PC=59,HS=59,BS=59,TC=59, [https://172.18.13.22:443/perf/private/v1/shopping_lists/me/c44ae5e4-7b89-11e8-8866-7d0ac1d19ef3/items]"
#data3 = "Tue Jul 03 2018 17:37:19 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi): tid(4354739)[172.18.6.14] gtid(c0873c625b3b982f004272b3): ExtLatency: TS=0,HR=0,BR=0,PS=0,ASV=0,AXF=1,ACO=1,ACO=1,AXF=3,ACO=3,AXF=9,ACL=40,AXF=40,ARE=40,ACO=40,PC=40,CS=40,HS=41,BS=41, == HR=41,BR=41,PS=41,ASV=41,AXF=42,AOE=42,ACO=42,AOE=42,ACO=42,AXF=42,ARE=42,ACO=42,AXF=42,PC=43,HS=43,BS=43,TC=43, [https://172.18.13.22:443/perf/private/v1/shopping_lists/me]"
#data4 = "Tue Jul 03 2018 17:38:39 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi): tid(3574693)[172.18.8.14] gtid(c0873c625b3b987f00368ba5): ExtLatency: TS=0,HR=0,BR=0,PS=0,ASV=0,AXF=0,ACO=0,ACO=0,AXF=3,ACO=3,AXF=9,ACL=40,AXF=40,ARE=41,ACO=41,PC=41,CS=41,HS=41,BS=41, == HR=41,BR=41,PS=41,ASV=41,AXF=42,AOE=42,ACO=42,AOE=42,ACO=42,AXF=42,ARE=43,ACO=43,AXF=43,PC=43,HS=43,BS=43,TC=43, [https://172.18.13.22:443/perf/private/v1/shopping_lists/me]"
#data5 = "Tue Jul 03 2018 17:30:33 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi): tid(3481365)[172.18.6.14] gtid(c0873c625b3b969900351f15): ExtLatency: TS=0,HR=0,BR=0,PS=0,ASV=0,AXF=1,ACO=1,ACO=1,AXF=3,ACO=3,AXF=9,ACL=38,AXF=39,ARE=39,ACO=39,PC=39,CS=39,HS=39,BS=39, == HR=39,BR=39,PS=39,ASV=39,AXF=40,AOE=40,ACO=40,AOE=40,ACO=40,AXF=41,ARE=41,ACO=41,AXF=41,PC=41,HS=41,BS=41,TC=41, [https://172.18.13.22:443/perf/private/v1/shopping_lists/me]"
#data6 = "Tue Jul 03 2018 17:36:05 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi): tid(3547285)[172.18.6.14] gtid(c0873c625b3b97e500362095): ExtLatency: TS=0,HR=0,BR=0,PS=0,ASV=0,AXF=1,ACO=1,ACO=1,AXF=4,ACO=4,AXF=9,ACL=48,AXF=49,ACO=49,PC=49,CS=49,BS=49,HS=49, == HR=49,BR=49,PS=49,ASV=49,AXF=50,AOE=50,ACO=50,AOE=50,ACO=50,AXF=51,ARE=51,ACO=51,AXF=51,PC=51,HS=51,BS=51,TC=51, [https://172.18.13.22:443/perf/private/v1/shopping_lists/me/c3359b54-7b89-11e8-8866-7d0ac1d19ef3/items/926ac026-7f7c-468a-a70d-a6ce7ffe143e]"
#data7 = "Tue Jul 03 2018 17:37:52 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi-internal): tid(2648561) gtid(c0873c625b3b9850002869f1): ExtLatency: TS=0,HR=0,BR=0,PS=0,AXF=0,ARE=0,PC=0,CS=0,HS=0,BS=0, == HR=37,BR=37,PS=37,ASV=37,AXF=38,PS=38,AXF=38,ARE=38,PC=38,ACL=38,ACO=38,PC=38,HS=38,BS=38,TC=38, [http://127.247.183.135:2444/x2020/v1/events/_bulk]"
#data8 = "Tue Jul 03 2018 17:39:15 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi-internal): tid(2661377) gtid(c0873c625b3b98a300289c01): ExtLatency: TS=0,HR=0,BR=0,PS=0,AXF=0,ARE=0,PC=0,CS=0,HS=1,BS=1, == HR=59,BR=81,PS=81,ASV=81,AXF=82,PS=82,AXF=82,ARE=82,PC=82,ACL=82,ACO=82,PC=82,HS=82,BS=82,TC=82, [http://127.247.183.135:2444/x2020/v1/events/_bulk]"
#data9 = "Tue Jul 03 2018 17:39:35 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi): tid(3587493)[172.18.8.14] gtid(c0873c625b3b98b70036bda5): ExtLatency: TS=0,HR=0,BR=0,PS=0,ASV=0,AXF=1,ACO=1,ACO=1,AXF=4,ACO=4,AXF=10,ACL=43,AXF=43,ACO=44,PC=44,CS=44,BS=44,HS=44, == HR=44,BR=44,PS=44,ASV=44,AXF=45,AOE=45,ACO=45,AOE=45,ACO=45,AXF=46,ARE=46,ACO=46,AXF=46,PC=46,HS=46,BS=46,TC=46, [https://172.18.13.22:443/perf/private/v1/shopping_lists/me/c1377a0c-7b89-11e8-8866-7d0ac1d19ef3/items/b37a947a-7add-4ddb-911f-ba8f6283ce91]"
#data10 = "Tue Jul 03 2018 17:35:07 [APIMgmt_B6B7F7B787][0x80e007ad][extlatency][info] mpgw(webapi-internal): tid(3536357) gtid(c0873c625b3b97ab0035f5e5): ExtLatency: TS=0,HR=0,BR=0,PS=0,AXF=1,ARE=1,PC=1,CS=1,HS=1,BS=1, == HR=40,BR=40,PS=40,ASV=40,AXF=40,PS=40,AXF=40,ARE=40,PC=40,ACL=40,ACO=40,PC=40,HS=40,BS=40,TC=40, [http://127.247.183.135:2444/x2020/v1/events/_bulk]"
#data = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]

data = []
file_object = open(r"C:\Users\IBM_ADMIN\Documents\Python\extLatencyLog.txt")
fileList = file_object.readlines()
for i in range(len(fileList)):
    file = fileList[i]
    data.append(file)

print(data)

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
            date1 = str(data[i])[0:24]
            use = data[i]
            date = datetime.strptime(date1, '%a %b %d %Y %H:%M:%S')
    unixDate = calendar.timegm(date.utctimetuple())
    xLabels.append(unixDate)

    step1 = use.split("ExtLatency: ")[1]
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

    array.pop()
    array.pop()
    number2 = []
    x = []
    y = [0.001]
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
        # print(str(titleCount) + "\t" + str(counter))
        # print(titleConst[titleCount] + "\t" + z[counter])
        tempv = titleConst[titleCount].translate(
            {ord(k): None for k in digits})
        # print(tempv)
        if (z[counter] == tempv):
            z[counter] = titleConst[titleCount]
            counter += 1
            titleCount += 1
            # print('---')
        else:
            titleCount += 1
            #print(z[counter])




 #   for i in range(len(z)):
 #      for o in range(len(titleConst)):
 #           if (z[i] == titleConst[o]) :
 #               z[i] = titleConst[o]
 #               break;
 #           else :
 #
 #           for j in range(len(z)):
 #               if i == j:
 #                   i = i
 #               elif z[i] == z[j]:
 #                   addon = 2
 #                   k = z[j] + str(addon)
 #                   if k in z:
 #                       while k in z:
 #                           addon += 1
 #                           k = z[j] + str(addon)
 #                       z[j] += str(addon)
 #                   else:
 #                       z[j] += str(addon)

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


# print(xAxis)
#print('-----***')
#print(len(xAxis))
# print(yAxis)
#print(len(yAxis))
# print(zAxis)
#print(len(zAxis))
#print('-----')
# for i in range(len(data)):
 #   print(len(xAxis[i]))
  #  print(len(yAxis[i]))
   # print(len(zAxis[i]))
    # if len(xAxis[i]) == len(yAxis[i]) == len(zAxis[i]):
     #   print("True")

biggest = yLabels[0]
for i in range(len(yLabels)):
    if len(biggest) < len(yLabels[i]):
        biggest = yLabels[i]

# for i in range(len(yLabels)):
 #   for j in range(len(yLabels[i])):
  #      if yLabels[i][j] not in biggest:
   #         biggest.append(yLabels[i][j])

title = {}
for i in range(len(titleConst)):
    title[titleConst[i]] = i + 1

yAxis2 = []
for i in range(len(data)):
    yAxis2.append([])
    for tc in range(len(titleConst)):
        for yl in range(len(yLabels[i])):
            if (yLabels[i][yl] == titleConst[tc]):
                #print (titleConst[tc]+"\t"+yLabels[i][yl]+" "+str(yl))
                yAxis2[i].append(title[titleConst[tc]])

        if (title[titleConst[tc]] not in yAxis2[i]):
            #print(str(title[titleConst[tc]])+" not in "+str(yAxis2[i]))
            yAxis2[i].append(title[titleConst[tc]])
            yAxis[i].insert(tc, -1)
            xAxis[i].insert(i, xAxis[i][0])

        # else:
        #    print(tc)
        #print(titleConst[tc] + "\t" + str(yAxis[i][yl]))
    # print('----')
    # print(yLabels[i])
    yAxis[i].insert(40, -1)
    xAxis[i].insert(40, xAxis[i][0])
# print(yAxis)
# print(yAxis2)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.xlim(1, len(data))

colours = ['k', 'r', 'm', 'b', 'c', 'g', 'y']
index = 0
legendLabels = []
addon2 = plt.Rectangle((0, 0), 2, 1, fc=colours[index])

for i in range(len(biggest)):
    addon2 = plt.Rectangle((0, 0), 2, 1, fc=colours[index])
    index += 1
    if index > len(colours) - 1:
        index = 0
    legendLabels.append(addon2)
#
#
# print(xAxis[0])
# print(yAxis[0])
# print(zAxis[0])
# print(yAxis2[0])
# print("-----")

#for i in range(len(data)):
 #   print(len(xAxis[i]))
  #  print(len(yAxis[i]))
   # print(len(yAxis2[i]))
    #if len(xAxis[i]) == len(yAxis[i]) == len(yAxis2[i]):
     #   print("True")
    #else:
     #   print("False")


colours2 = ['k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g',
            'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y', 'k', 'r', 'm', 'b', 'c', 'g', 'y','k']
for i in range(len(data)):
    ax.bar(xAxis[i], yAxis[i], yAxis2[i], zdir='y',
           color=colours2, edgecolor=colours2, alpha=0.5, width=1)
    # print(xAxis[i])
    # print(yAxis[i])
    # print(zAxis[i])
    # print(yAxis2[i])
    # print("-----")


#for i in range(len(data)):
 #   px = ""
  #  py = ""
   # py2 = ""
    #pL = ""
    #for j in range(len(xAxis[i])):
     #   px = px +"\t"+str(xAxis[i][j])
      #  py = py + "\t" + str(yAxis[i][j])
       # py2 = py2 + "\t" + str(yAxis2[i][j])
        #pL = pL + "\t" + str(titleConst[j])

    # print(pL)
    # print(py)
    # print(py2)
    # print("------")
figsize = (len(data), len(zAxis[0]))
ax.legend(legendLabels, biggest)
ax.w_yaxis.set_ticklabels("")
ax.w_xaxis.set_ticklabels(xLabels)
ax.set_xlabel('Timestamp')
ax.set_ylabel('Stage')
ax.set_zlabel('value')
#print(biggest)
plt.show()

#
# read from a file
