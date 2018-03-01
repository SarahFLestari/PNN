import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
import math

x = []
y = []
z = []
q = []
class0 = []
class1 = []
class2 = []

file = open('data_train_PNN.txt')

with open('data_train_PNN.txt') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    z = [float(line.split()[2]) for line in lines]
    q = [int(line.split()[3]) for line in lines]

for i in range(len(q)) :
    # print(i)
    if (q[i] == 0):
        class0.append([x[i],y[i],z[i]])
    elif (q[i] == 1):
        class1.append([x[i],y[i],z[i]])
    elif (q[i] == 2):
        class2.append([x[i],y[i],z[i]])

def euclid (x1,y1,z1,x2,y2,z2):
    hasil = math.sqrt((math.pow(x2-x1,2))+(math.pow(y2-y1,2))+(math.pow(z2-z1,2)))
    return hasil

fig = pyplot.figure()
ax = Axes3D(fig)

for i in range(len(class0)):
    for j in range(0,len(class0)):
        if (i != j):
            # print("i", i, "j", j)
            minClass0 = []
            x= euclid(class0[i][0],class0[i][1],class0[i][2],class0[j][0],class0[j][1],class0[j][2])
            # print((class0[i][0],class0[i][1],class0[i][2],class0[j][0],class0[j][1],class0[j][2]))
            # print(x)
            minClass0.append(x)
            minClass0.sort()
    daftarMinClass0 = []
    daftarMinClass0.append(minClass0[0])

sumMinClass0 = sum(daftarMinClass0)
avgDistClass0 = (1/46) * sumMinClass0
print("average distance 0 ", avgDistClass0)

for i in range(len(class1)):
    for j in range(0,len(class1)):
        if (i != j):
            # print("i", i, "j", j)
            minClass1 = []
            x= euclid(class1[i][0],class1[i][1],class1[i][2],class1[j][0],class1[j][1],class1[j][2])
            # print(class1[i][0],class1[i][1],class1[i][2],class1[j][0],class1[j][1],class1[j][2])
            # print(x)
            minClass1.append(x)
            minClass1.sort()
    daftarMinClass1 = []
    daftarMinClass1.append(minClass1[0])

sumMinClass1 = sum(daftarMinClass1)
avgDistClass1 = (1/48) * sumMinClass1
print("average distance 1 ",avgDistClass1)

for i in range(len(class2)):
    for j in range(0,len(class2)):
        if (i != j):
            # print("i", i, "j", j)
            minClass2 = []
            x= euclid(class2[i][0],class2[i][1],class2[i][2],class2[j][0],class2[j][1],class2[j][2])
            # print(class1[i][0],class1[i][1],class1[i][2],class1[j][0],class1[j][1],class1[j][2])
            # print(x)
            minClass2.append(x)
            minClass2.sort()
    daftarMinClass2 = []
    daftarMinClass2.append(minClass2[0])

sumMinClass2 = sum(daftarMinClass2)
avgDistClass2 = (1/56) * sumMinClass2
print("average distance 2 ",avgDistClass2)

g = 0.11

touClass0 = g * avgDistClass0
touClass1 = g * avgDistClass1
touClass2 = g * avgDistClass2
print("tou0 ",touClass0)
print("tou1 ",touClass1)
print("tou2 ",touClass2)

ax.set_xlabel("atribut 1")
ax.set_ylabel("atribut 2")
ax.set_zlabel("atribut 3")

for i in range(len(class0)):
    ax.scatter(class0[i][0], class0[i][1], class0[i][2], color='r')
for i in range(len(class1)):
    ax.scatter(class1[i][0], class1[i][1], class1[i][2], color='g')
for i in range(len(class2)):
    ax.scatter(class2[i][0], class2[i][1], class2[i][2], color='b')
pyplot.title('Visualisasi data training')
pyplot.show()



# def rataDistance():
