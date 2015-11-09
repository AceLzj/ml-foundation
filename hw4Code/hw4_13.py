import numpy
fp = open("ntumlone_hw4_hw4_train.dat", "r")
xD_train = []
yD_train = []
xD_val = []
yD_val = []
train_data_len = 0
val_data_len = 0
data_len = 0
x_train = []
y_train = []
def sign(num):
    if num > 0:
       return 1
    else:
       return -1
for line in fp:
    data = line.split()
    if data == []:
         break
    data = [1] + data
    if train_data_len < 120:
         xD_train.append(data[:-1])
         yD_train.append(int(data[-1]))
         x_train.append(data[:-1])
         y_train.append(int(data[-1]))
         train_data_len += 1
         data_len += 1
    else:
         xD_val.append(data[:-1])
         yD_val.append(int(data[-1]))
         x_train.append(data[:-1])
         y_train.append(int(data[-1]))
         val_data_len += 1
         data_len += 1
print train_data_len
print val_data_len
fp.close()
fp = open("ntumlone_hw4_hw4_test.dat", "r")
x_test = []
y_test = []
test_data_len = 0
for line in fp:
    data = line.split()
    if data == []:
         break
    data = [1] + data
    x_test.append(data[:-1])
    y_test.append(int(data[-1]))
    test_data_len += 1
fp.close()
Lambdas = [100,10,1,10**-1,10**-2,10**-3,10**-4,10**-5,10**-6,10**-7,10**-8]
xD_train = numpy.asarray(xD_train,dtype = float)
x_train = numpy.asarray(x_train,dtype = float)
xD_val = numpy.asarray(xD_val,dtype = float)
x_test = numpy.asarray(x_test,dtype = float)
(n, m) = xD_train.shape
I = numpy.identity(m)
print I
bestLambda = 0
minEin = 1
Eout = 0
Eval = 0
minEval = 1
minEout = 1
bestWreg = 0
for Lambda in Lambdas:
    Wreg = numpy.linalg.inv((xD_train.transpose().dot(xD_train) + I*Lambda)).dot(xD_train.transpose()).dot(yD_train)
    errorsTest = 0
    errorsTrain = 0
    errorsVal = 0
    for i in range(train_data_len):
        if sign(Wreg.T.dot(xD_train[i])) != yD_train[i]:
           errorsTrain += 1
    for i in range(val_data_len):
        if sign(Wreg.T.dot(xD_val[i])) != yD_val[i]:
           errorsVal += 1
    for i in range(test_data_len):
        if sign(Wreg.transpose().dot(x_test[i])) != y_test[i]:
           errorsTest += 1
    tempEval = float(errorsVal) / float(val_data_len)   
    if tempEval < minEval:
        Eout = float(errorsTest) / float(test_data_len)
        Eval = float(errorsVal) / float(val_data_len)
        Ein = float(errorsTrain) / float(train_data_len)
        bestLambda = Lambda
        minEval = tempEval
        bestWreg = Wreg
errorsTrain = 0
errorsTest = 0 
Wreg = numpy.linalg.inv((x_train.transpose().dot(x_train) + I*bestLambda)).dot(x_train.transpose()).dot(y_train)
print Wreg
for i in range(data_len):
    if sign(Wreg.T.dot(x_train[i])) != y_train[i]:
        errorsTrain += 1
for i in range(test_data_len):
    if sign(Wreg.T.dot(x_test[i])) != y_test[i]:
        errorsTest += 1
print float(errorsTrain) / float(data_len)
print float(errorsTest) / float(test_data_len)
print bestLambda,Ein,Eval,Eout
