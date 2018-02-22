from pandas import Series
from pandas import DataFrame

# Reindexing Series
obj = Series([100,200,300,400,500], index = ['d','a','b','e','c'])
print("Original Index\n",obj)
print("\n")

# reindexing
obj = obj.reindex(['a','b','c','d','e'])
print("Reindexed DataFrame is\n",obj)
print("\n")

# Reindexing DataFrame
data = {'Name':['John','Tim','Rob'],
        'Age': ['34','23','42'],
        'Salary':[4500,2300,5800]
        }

frame = DataFrame(data)
print("Original Dataframe")
print(frame)
print("\n")

# reindexing Rows
frame = frame.reindex([0,2,1])
print("Reindexed Frame")
print(frame)
print("\n")

# reindexing Columns
frame = frame.reindex(columns = ['Name','Age','Salary'])
print("Reindexed Columns")
print(frame)
print("\n")