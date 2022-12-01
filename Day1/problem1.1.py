
# Open file, read lines and close file
file1 = open('input1.txt', 'r')
Lines = file1.readlines()
file1.close

# Create variables
max = 0
sum = 0

# Sum all the values until reach a empty line and get the maximum sum value of all the blocks
for line in Lines:
    if line == '\n':
        if sum > max:
            max = sum
        sum = 0
    else:
        sum += (int(line, base=10))
print(max)