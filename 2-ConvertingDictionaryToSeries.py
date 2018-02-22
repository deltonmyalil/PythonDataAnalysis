from pandas import Series
salary = {'John':3000, 'Tim':4500,'Rob':5600}
print(salary)

se3 = Series(salary) #Converting dictionary into Series using: <serName> = Series(<dictName>)
print(se3) # now the key becommes index

print("Using Series "+str(se3['Tim'])) #Printing using index 'Tim'
print("Using Dictionary key",salary['Tim'])