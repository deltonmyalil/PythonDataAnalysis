from pandas import Series
from pandas import DataFrame

# Arithmetic Operations on Series
# Both series are having same no of items
print("On Series\n")
series1 = Series([1, 2, 3, 4, 5])
series2 = Series([100, 200, 300, 400, 500])
print(series1 + series2)
print("\n")

# Both series are having different elements
series1 = Series([1, 2, 3, 4, 5])
series2 = Series([100, 200, 300, 400, 500, 600])
print(series1 + series2)
print("\n")  # We get NaN in the last entry

# Arithmetic operation on DataFrames
print("On DataFrames\n")
data1 = {
    'Speed': [100, 103, 105],
    'Temp': [34, 23, 42]
}
frame1 = DataFrame(data1)
print("\nDataFrame1")
print(frame1)

data2 = {
    'Speed': [101, 109, 106],
    'Temp': [34, 23, 42],
    'Humidity': [45, 23, 58]
}
frame2 = DataFrame(data2)
print("\nDataFrame2")
print(frame2)

# Adding these two
print("\nSum is:")
print(frame1+frame2)  # youll get humidity as NaN