from pandas import DataFrame

data2 = {
    'Speed': [101, 109, 106],
    'Temp': [34, 23, 42],
    'Humidity': [45, 23, 58]
}
frame2 = DataFrame(data2)

print(frame2)

print(frame2.sum())  # Finding sum of attributes

print(frame2.sum(axis=1))  # Finding sum of tuples

print(frame2.idxmax())  # Which tuple has the max Speed, Humidity and Temp (returns respective indices
print(frame2.idxmin())
print(frame2.max())  # Which is the maximum recorded value of Hum, Temp, Speed
