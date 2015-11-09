import random
import math
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
test_time = 5000
Ein_sum = 0
Eout_sum = 0
for i in range(test_time):
    x = []
    y = []
    for j in range(20):
        x.append(random.uniform(-1,1))
    x.sort()
    for j in range(20):
        tmp = random.uniform(0,1)
        if tmp <= 0.2:
           y.append(-sign(x))
        else:
           y.append(sign(x))
    Theta = generateTheta(x)
    bestEin = 1
    bestEout = 1
    for s in [-1,1]:
        for theta in Theta:
            Ein = calEin(s,theta,x,y)
            Eout = calEout(s,theta)
            if Ein < bestEin:
                bestEin = Ein
            if Eout < bestEout:
                bestEout = Eout
    Ein_sum += bestEin
    Eout_sum += bestEout
print float(Ein_sum) / float(test_time)
print float(Eout_sum) / float(test_time)
