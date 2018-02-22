from pandas import Series
#from pandas import DataFrame

series = Series([100,200,300], index=['a','b','b'])
print(series)  # Has duplicates

# Duplicate check
print(series.index.is_unique)  # For checking uniqueness of index
print(series.is_unique)  # Fro checking uniqueness of the series itself (values)