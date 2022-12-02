# Create class to each element
class X:
    score = 1
    clashes = {
        "A" : 3,
        "B" : 0,
        "C" : 6
    }

class Y:
    score = 2
    clashes = {
        "A" : 6,
        "B" : 3,
        "C" : 0
    }

class Z:
    score = 3 
    clashes = {
        "A" : 0,
        "B" : 6,
        "C" : 3
    }

def total_score():
    # Open file, read lines and close file
    file1 = open('input2.txt', 'r')
    Lines = file1.readlines()
    file1.close

    sum = 0
    for line in Lines:
        pair = line.split()
        
        score = 0
        first = pair[0] # Get element first column
        second = pair[1] # Get element secound column
        
        # Calculate score
        match second:
            case "X":
                score = X.score + X.clashes.get(first)
            case "Y":
                score = Y.score + Y.clashes.get(first)
            case "Z":
                score = Z.score + Z.clashes.get(first)
        
        sum += score

    return sum


if __name__ == "__main__":
    print(total_score())


