import numpy
a = numpy.arange(0,60,5)
a = a.reshape(3,4)
print(a)

for x in numpy.nditer(a):
    print(x)  # To traverse the array - single or multidim; use nditer method