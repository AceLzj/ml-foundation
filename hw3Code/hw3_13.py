import random
import numpy
def sign(num):
    if num > 0:
        return 1
    else:
        return -1
def calEin(data_len,Y,Wlin,X):
    errors = 0
    for i in range(data_len):
        y = sign(X[i].dot(Wlin))
        yi = int(Y[i])
        if yi != y:
           errors += 1
    return float(errors) / float(data_len)
Ein = 0
expriment_time = 1000
data_len = 1000
H = {}
min_errors = 1
bestWlin = 1
"""
for i in range(expriment_time):
    X = []
    Y = []
    min_errors = 1
    for j in range(data_len):
        x1 = random.uniform(-1,1)
        x2 = random.uniform(-1,1)
        y = sign(x1**2+x2**2-0.6)
        p = random.uniform(0,1)
        if p <= 0.1:
           y*=-1
        X.append([1,x1,x2,x1*x2,x1*x1,x2*x2])
        Y.append([y])
    Xarray = numpy.asarray(X)
    Yarray = numpy.asarray(Y)
    Wlin = numpy.linalg.pinv(Xarray).dot(Yarray)
    print Wlin
    errors = calEin(data_len,Yarray,Wlin,Xarray)
    if errors < min_errors:
       bestWlin = Wlin
    Ein += errors
"""

Ein = 0
for i in range(expriment_time):
    X = []
    Y = []
    for j in range(data_len):
        x1 = random.uniform(-1,1)
        x2 = random.uniform(-1,1)
        y = sign(x1**2+x2**2-0.6)
        p = random.uniform(0,1)
        if p <= 0.1:
           y*=-1
        X.append([1,x1,x2,x1*x2,x1*x1,x2*x2])
        Y.append([y])
    Xarray = numpy.asarray(X)
    Yarray = numpy.asarray(Y)
    Wlin = numpy.asarray([[-1],[-0.05],[0.08],[0.13],[1.5],[1.5]],dtype = float)
    errors = calEin(data_len,Yarray,Wlin,Xarray)
    Ein += errors

print float(Ein) / float(expriment_time)
