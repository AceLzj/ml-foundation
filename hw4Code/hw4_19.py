import numpy
fp = open("ntumlone_hw4_hw4_train.dat", "r")
val1 = []
val2 = []
val3 = []
val4 = []
val5 = []
train_data_len = 0
val1_len = 0
val2_len = 0
val3_len = 0
val4_len = 0
val5_len = 0
data_len = 0
train = []
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
    if val1_len < 40:
         val1.append((data[:-1],int(data[-1])))
         train.append((data[:-1],int(data[-1])))
         x_train.append(data[:-1])
         y_train.append(int(data[-1]))
         data_len += 1
         val1_len += 1
    elif val2_len < 40:
         val2.append((data[:-1],int(data[-1])))
         train.append((data[:-1],int(data[-1])))
         x_train.append(data[:-1])
         y_train.append(int(data[-1]))
         val2_len += 1
         data_len += 1
    elif val3_len < 40:
         val3.append((data[:-1],int(data[-1])))
         train.append((data[:-1],int(data[-1])))
         x_train.append(data[:-1])
         y_train.append(int(data[-1]))
         val3_len += 1
         data_len += 1
    elif val4_len < 40:
         val4.append((data[:-1],int(data[-1])))
         train.append((data[:-1],int(data[-1])))
         x_train.append(data[:-1])
         y_train.append(int(data[-1]))
         val4_len += 1
         data_len += 1
    elif val5_len < 40:
         val5.append((data[:-1],int(data[-1])))
         train.append((data[:-1],int(data[-1])))
         x_train.append(data[:-1])
         y_train.append(int(data[-1]))
         val5_len += 1
         data_len += 1
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
CVtrain = []
CVtrain.append(train[40:])
CVtrain.append(train[0:40]+train[80:])
CVtrain.append(train[0:80]+train[120:])
CVtrain.append(train[0:120]+train[160:])
CVtrain.append(train[0:160])
CVal = []
CVal.append(val1)
CVal.append(val2)
CVal.append(val3)
CVal.append(val4)
CVal.append(val5)
bestLambda = 0
minCVerrors = 1
Eout = 0
Eval = 0
minEval = 1
minEout = 1
bestWreg = 0
for Lambda in Lambdas:
    CVerrors = 0
    i = 0
    for trainData in CVtrain:
        xTrain = []
        yTrain = []
        for data in trainData:
            xTrain.append(data[0])
            yTrain.append(data[1])
        xD_train = numpy.asarray(x_train,dtype = float)
        yD_train = numpy.asarray(y_train,dtype = float)
        (n,m) = xD_train.shape
        I = numpy.identity(m)
        Wreg = numpy.linalg.inv((xD_train.transpose().dot(xD_train) + I*Lambda)).dot(xD_train.transpose()).dot(yD_train)
        errorsTest = 0
        errorsTrain = 0
        errorsVal = 0
        for testData in CVal[i]:
                xD_val = testData[0]
                yD_val = testData[1]
                xD_val = numpy.asarray(xD_val,dtype = float)
                if sign(Wreg.T.dot(xD_val)) != yD_val:
                  CVerrors += 1
        i += 1
    tempCVerrors = float(CVerrors) / float(200)   
    if tempCVerrors < minCVerrors:
        bestLambda = Lambda
        minCVerrors = tempCVerrors
        bestWreg = Wreg
print bestLambda,minCVerrors
errorsTrain = 0
errorsTest = 0
x_train = numpy.asarray(x_train,dtype = float)
x_test = numpy.asarray(x_test,dtype = float)
Wreg = numpy.linalg.inv((x_train.transpose().dot(x_train) + I*bestLambda)).dot(x_train.transpose()).dot(y_train)
print len(x_train)
for i in range(data_len):
    print i
    if sign(Wreg.T.dot(x_train[i])) != y_train[i]:
        errorsTrain += 1
for i in range(test_data_len):
    print i
    if sign(Wreg.T.dot(x_test[i])) != y_test[i]:
        errorsTest += 1
print float(errorsTrain) / float(data_len)
print float(errorsTest) / float(test_data_len)
#print bestLambda,Ein,Eval,Eout
