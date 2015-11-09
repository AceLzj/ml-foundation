import numpy
import random
from numpy import*
fp = open("hw1_18_train.txt","r")
def sign(num):
    if num > 0:
        return 1
    else:
        return -1
def shuffle(random_seed,training_data):
    new_training_data = []
    random.seed(random_seed)
    tmp_data = training_data[:]
    l = len(training_data)
    l1 = len(training_data) 
    i = 0
    while i < l:
        ran = int(random.uniform(0,l1))
        new_training_data.append(tmp_data[ran])
        del tmp_data[ran]
        l1 -= 1
        i += 1
    return new_training_data
training_data = []
for line in fp:
        data = line.split()
        if data == []:
            break
        training_data.append((data[:4],data[-1]))
fp.close()
fp = open("hw1_18_test.txt","r")
test_data = []
for line in fp:
        data = line.split()
        if data == []:
            break
        test_data.append((data[:4],data[-1]))
fp.close()
errors = 0
w = array([[0],[0],[0],[0],[0]])
errors = 0
l = len(training_data)
for i in range(l):
   data = training_data[i]
   x = numpy.asarray([[1],[data[0][0]],[data[0][1]],[data[0][2]],[data[0][3]]],dtype = float)
   y = int(data[1])
   if sign((transpose(w).dot(x))) != y:
       errors += 1
update = 0
training_time = 2000
all_errors = 0
l1 = len(test_data)
for i in range(training_time):
   w = array([[0],[0],[0],[0],[0]])
   new_training_data = shuffle(i,training_data)
   l = len(new_training_data)
   j = 0
   total = 0
   stopAt = -1
   while update < 100:
            data = new_training_data[j]
            x = numpy.asarray([[1],[data[0][0]],[data[0][1]],[data[0][2]],[data[0][3]]],dtype = float)
            y = int(data[1])
            if sign((transpose(w).dot(x))) != y:
                  w = w + y*x
                  stopAt = j
                  min_errors = 0
                  for i in range(l):
                         data = training_data[i]
                         x = numpy.asarray([[1],[data[0][0]],[data[0][1]],[data[0][2]],[data[0][3]]],dtype = float)
                         y = int(data[1])
                         if sign((transpose(w).dot(x))) != y:
                             min_errors += 1
                  if min_errors < errors:
                         w_best = w
                         errors = min_errors
                  j = (j + 1) % l
                  update += 1
                  continue
            else:
                  j = (j + 1) % l
            if stopAt == j:
                  break
   for k in range(l1):
             data = test_data[k]
             x = numpy.asarray([[1],[data[0][0]],[data[0][1]],[data[0][2]],[data[0][3]]],dtype = float)
             y = int(data[1])
             if sign((transpose(w_best).dot(x))) != y:
                  all_errors += 1
print float(all_errors) / float(training_time*l1)
