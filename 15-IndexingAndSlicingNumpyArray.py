import numpy

a = numpy.arange(10)
print(a)

s = slice(2, 7, 2)  # start = 2, end = 7, step = 2
print(a[s])

b = a[2:7:2]  # another way to slice
print(b)

print(a[2::-1])
print(a[2:8])  # etc as in list slicing

# Multidim array
print("\n MultidimArray")
a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
# Selecting from MultiDim array
print("Result is",a[[0,1,2],[0,1,0]])  # 0th el inn 0th array, 1st el in 1st array, 0th el in 2nd array
print(a[0,1])  # 0th array, 1st el = 2

x = numpy.array([[0,0],[2,2]])
y = numpy.array([[2,0],[0,2]])
cornerEls = a[x,y]
print("\nCorner Elements are :\n",cornerEls)

# Boolean indexing
# Eg: print array elements greater than 5

print("\nGreater than 5 els are",a[a>5])