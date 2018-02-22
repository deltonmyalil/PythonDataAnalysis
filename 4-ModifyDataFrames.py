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

# adding another new column to table
nextFrame = DataFrame(data, columns=['Name','Age','Salary','NewColumn']) # user defined additional column
print(nextFrame)
print("\n")

# Adding values to new column
nextFrame['NewColumn'] = 'Doctor'
print(nextFrame)
print("\n")

# Adding individual distinct values to new column
nextFrame['NewColumn'] = ['Doctor','Lawyer','Engineer']
print(nextFrame)
print("\n")

# Adding new Column with values
nextFrame['Education'] = 'MS'
print(nextFrame)
print("\n")

# Transposing a frame
transposeFrame = nextFrame.T
print(transposeFrame)