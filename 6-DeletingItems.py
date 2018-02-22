from pandas import DataFrame

data = {'Name': ['John', 'Tim', 'Rob'],
        'Age': ['34', '23', '42'],
        'Salary': [4500, 2300, 5800]
        }

frame = DataFrame(data)
print("Original Dataframe")
print(frame)
print("\n")

# reindexing Rows
frame = frame.reindex([0, 2, 1])
print("Reindexed Frame")
print(frame)
print("\n")

# reindexing Columns
frame = frame.reindex(columns=['Name', 'Age', 'Salary'])
print("Reindexed Columns")
print(frame)
print("\n")

# Deleting a tuple
frame2 = frame.drop([2]) #specifying row index
print("Deleted tuple 2")
print(frame2)
print("\n")

#Deleting multiple tuples
frame3 = frame.drop([1,2])
print(frame3)
print("\n")

# Deleting columns
frame3 = frame.drop('Salary', axis=1)  # axis = 1 specifies column, you need to define axis = 1 for deleting column
print(frame3)
print("\n")