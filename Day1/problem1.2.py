# Import numpy
import numpy as np

# Open file, read lines and close file
file1 = open('input1.txt', 'r')
Lines = file1.readlines()
file1.close

# Create variables
sum = 0
max = 0
sum_values = []

# Iterate each line and sum all the values until get a empty line
for line in Lines:
    if line == '\n':
        sum_values.append(sum)
        sum = 0
    else:
        sum += (int(line, base=10))

# Sort the array, get the 3 max values and then sum them.
sum_values = np.sort(sum_values)
top3 = sum_values[-3:]
print(np.sum(top3))