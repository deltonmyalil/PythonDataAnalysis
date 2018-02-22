from pandas import Series
from pandas import DataFrame

ser = Series([3,7,1,4,7,2], index=[2,7,3,5,9,1])
print(ser)
print("\nSorting")
print(ser.sort_index())

data2 = {
    'Speed': [101, 109, 106],
    'Temp': [34, 23, 42],
    'Humidity': [45, 23, 58]
}
frame2 = DataFrame(data2)
print("\nSorting\n")
frame2 = frame2.reindex([2,1,0])  # Just reindexing to make it unsorted first
print(frame2)
print("\nRows Sorted to:")
print((frame2.sort_index()))  # Sorting rows
frame2 = frame2.reindex(columns=['Speed','Humidity','Temp'])  # Reindexing to make columns unsorted
print(frame2)
print("\nColumns Sorted to:")
frame2 = frame2.sort_index(axis = 1)  # Axis = 1 specifies column

#  Sorting in the descending order
desc = frame2.sort_index(ascending=False)
print(desc)
desc = frame2.sort_index(axis=1,ascending=False)
print(desc)

# Sorting according to their values
# Instead of sort_index(), use sort_values()
print("\nSorting according to values")
print(ser.sort_values())  # For a series

print("\nSorting according to values of a DF")
print(frame2.sort_values(by='Humidity'))  # For a DF sort by an attrib