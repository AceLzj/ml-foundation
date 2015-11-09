import numpy
import math
fp = open("ntumlone_hw3_hw3_train.dat", "r")
x_train = []
y_train = []
data_len = 0
def sign(num):
    if num > 0:
       return 1
    else:
       return -1
for line in fp:
    data = line.split()
    if data == []:
         break
    x_train.append(data[:-1])
    y_train.append(int(data[-1]))
    data_len += 1
fp.close()
fp = open("ntumlone_hw3_hw3_test.dat", "r")
x_test = []
y_test = []
test_data_len = 0
for line in fp:
    data = line.split()
    if data == []:
         break
    x_test.append(data[:-1])
    y_test.append(int(data[-1]))
    test_data_len += 1
fp.close()
T = 2000
n = 0.01
def calGradient(x,y,w,n):
    L = []
    dim = len(x[0])
    for i in range(dim+1):
        L.append([0])
    s = numpy.asarray(L,dtype = float)
    tmp = len(x[n])
    tmpxn = [[1]]
    for j in range(tmp):
            tmpxn.append([x[n][j]])
    xn = numpy.asarray(tmpxn,dtype = float)
    SGradient = float(1) / float((1+math.exp((-1)*float((-1)*y[n]*w.transpose().dot(xn)))))*((-1)*y[n]*xn)
    return SGradient
L = []
dim = len(x_train[0])
for i in range(dim+1):
    L.append([0])
w = numpy.asarray(L)
num = 0
for i in range(T):
    w = w - n*calGradient(x_train,y_train,w,num)
    num = (num + 1) % data_len
print w
Eout = 0
print test_data_len
for i in range(test_data_len):
    tmp = len(x_test[i])
    tmpxi = [[1]]
    for j in range(tmp):
       tmpxi.append([x_test[i][j]])
    xi = numpy.asarray(tmpxi,dtype = float)
    if sign(w.transpose().dot(xi)) != y_test[i]:
       Eout += 1
print Eout
