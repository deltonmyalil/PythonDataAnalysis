from pandas import DataFrame
from pandas import Series
import numpy  # import numpy as sasi - then you can call it as sasi.nan instead of numpy.nan

# For Series
ser = Series([1,2,3,4,numpy.nan],index=['a','b','c','d','e'])
print(ser)

print("Dropping NaN\n")
print(ser.dropna())  # It just deleted the index and value containing NaN

# For DataFrame
frame2 = DataFrame({
    'Speed': [101, numpy.nan, 106],
    'Temp': [34, 23, 42],
    'Humidity': [45, numpy.nan, 58]
})
print(frame2)
print(frame2.dropna())  # But the entire tuple is gone even though there were only 2 NaNs
print(frame2.fillna(0))  # Replaced NaN with 0, so the tuple is saved from dropping
