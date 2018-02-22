#Data frame is like the Series but with two indices ie row index and column index
from pandas import DataFrame

data = {'Name':['John','Tim','Rob'],
        'Age': ['34','23','42'],
        'Salary':[4500,2300,5800]
        }

frame = DataFrame(data)
print(frame)  # Note that the output has two indices - row:[0,1,2], column:[Age,Name,Sal]
print("\n")  # also note that the indices age, sal etc are arranged alphabetically

# We need to change the column sequence from alphabetic order
newFrame = DataFrame(data, columns=['Name','Age','Salary'])  # user defined columns
print(newFrame)
print("\n")

# adding another value to table
nextFrame = DataFrame(data, columns=['Name','Age','Salary','NewColumn']) # user defined additional column
print(nextFrame)
print("\n")

# Retrieving values from columns
print(newFrame['Salary'])
print("\n")

# Retrieving values from rows - x axis = ix
print(newFrame.ix[2])  # indexXaxis[2]
print("\n")