import random
import math
fp = open("hw2_training_data", "r")
training_data = []
for line in fp:
    data = line.split()
    if data == []:
         break
    training_data.append((data[:9],data[-1]))
fp.close()
test_data = []
fp = open("hw2_test_data", "r")
for line in fp:
    data = line.split()
    if data == []:
         break
    test_data.append((data[:9],data[-1]))
fp.close()
def calEout(s,theta):
    return 0.5 + 0.3*s*(abs(theta) - 1)
def sign(x):
    if x > 0:
       return 1
    else:
       return -1
def calEin(s,theta,x,y):
    h = []
    Ein = 0
    for xi in x:
        h.append(s*sign(xi-theta))
    l = len(h)
    for i in range(l):
        if h[i] != y[i]:
           Ein += 1
    return float(Ein) / float(l)
def generateTheta(x):
    l = len(x)
    theta = []
    for i in range(l-1):
        theta.append(x[i] + x[i+1] / 2)
    return theta
bestEin = 1
best_dim = 0
best_s = 0
best_theta = 0
for i in range(9):
    x = []
    y = []
    tmp_data = training_data[:]
    tmp_data.sort(key = lambda x:x[0][i])
    for data in tmp_data:
        tmp1 = float(data[0][i])
        tmp2 = int(data[1])
        x.append(tmp1)
        y.append(tmp2)     
    Theta = generateTheta(x)
    bestEout = 1
    for s in [-1,1]:
        for theta in Theta:
            Ein = calEin(s,theta,x,y)
            if Ein < bestEin:
                bestEin = Ein
                best_dim = i
                best_s = s
                best_theta = theta
tmp_data = test_data[:]
tmp_data.sort(key = lambda x:x[0][best_dim])
bestEout = 1
for data in tmp_data:
    tmp1 = float(data[0][best_dim])
    tmp2 = int(data[1])
    x.append(tmp1)
    y.append(tmp2) 
Eout = calEin(best_s,best_theta,x,y)
print float(Eout)
