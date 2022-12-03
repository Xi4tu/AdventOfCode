import string

def totalPriority():
    # Open file, read lines and close file
    file1 = open('input3.txt', 'r')
    Lines = file1.readlines()
    file1.close

    # Variables
    priorities = dict(zip(string.ascii_letters, range(len(string.ascii_letters)))) # {a:0, b:1, c:2 ...}
    l = [] 
    i = 0
    sum = 0
    
    # Iterate each line, make group of 3 lines, then do the intersection of the 3 string to get the character in common
    # and then get the priority of the character
    for line in Lines:
        i = i + 1
        l.append(line.strip())
        if i == 3:
            character = set(l[0]).intersection(l[1]).intersection(l[2]).pop()
            sum += priorities.get(character) + 1
            l.clear()
            i = 0
            continue
    
    return sum

if __name__ == "__main__":
    print(totalPriority()) 
