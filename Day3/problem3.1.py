# Import textwrap to divide string
import textwrap
import string

def totalPriority():
    # Open file, read lines and close file
    file1 = open('input3.txt', 'r')
    Lines = file1.readlines()
    file1.close

    priorities = dict(zip(string.ascii_letters, range(len(string.ascii_letters))))  # {a:0, b:1, c:2 ...}
    sum = 0 # Store priorities sum
    for line in Lines:
        # Divide in 2 parts
        parts = textwrap.wrap(line, int(len(line)/2))

        # store character in common
        character = ""

        # Check characters
        character = set(parts[0]).intersection(parts[1]).pop()
        # Acumulate priority of the character
        sum += priorities.get(character) + 1
    
    return sum

if __name__ == "__main__":
    print(totalPriority())