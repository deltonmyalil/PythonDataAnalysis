import numpy
a = numpy.array([1,2,3,4])
b = numpy.array([10,20,30,40])
c = a * b  # Two array have the same shape
print(c)

# For Different shapes, we have to broadcast
a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
b = numpy.array([1,2,3])
print(a+b)  # b gets added to each elements of a