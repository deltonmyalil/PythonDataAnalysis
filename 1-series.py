from pandas import Series
se1 = Series([1,2,3,4,5])#Series is kinda like a list but with some exceptions
print(se1)
print(se1[2])

se2 = Series([100,200,300],index = ['a','b','c']) #one of the exception is that you can specify custom indexes
print(se2)
print(se2['b']) # printing using the custom index