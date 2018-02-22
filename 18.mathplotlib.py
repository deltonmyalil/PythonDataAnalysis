# Line : y = mx + c
import numpy
import math
from matplotlib import pyplot

#x = numpy.arange(1,11)
x = numpy.arange(1,11)
y = 4 * x + 5

pyplot.title("This is the title")
pyplot.xlabel("This is x label")
pyplot.ylabel("This is y label")
pyplot.plot(x,y)
pyplot.show()