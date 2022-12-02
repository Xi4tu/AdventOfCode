# Create class to each element
class A: # Rock
    score = 1
    clashes = { 
        "win" : 2, # -> The score of the shape that wins against A(rock)
        "draw" : 1,
        "loss" : 3
    }

class B: # Paper
    score = 2
    clashes = { 
        "win" : 3, # -> The score of the shape that wins against B(Paper)
        "draw" : 2,
        "loss" : 1
    }

class C: # Scissors
    score = 3
    clashes = { 
        "win" : 1, # -> The score of the shape that wins against C(Scissors)
        "draw" : 3,
        "loss" : 2
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
            case "X": # Loss
                score = shapeScore(first, "loss") + 0
            case "Y": # Draw
                score = shapeScore(first, "draw") + 3
            case "Z": # Win
                score = shapeScore(first, "win") + 6
        
        sum += score

    return sum

# Returns the score of the shape that provides the result
def shapeScore(shape, result):
    match shape:
        case "A":
            return A.clashes.get(result)
        case "B":
            return B.clashes.get(result)
        case "C":
            return C.clashes.get(result)


if __name__ == "__main__":
    print(total_score())