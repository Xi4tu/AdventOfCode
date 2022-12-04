def totalContainedPairs(filename):
    # Open file
    with open(filename) as f:
        count = 0

        # Process each line of the file
        for line in f:
            # assignments = ['x1-y1','x2-y2']
            assignments = line.strip().split(",")

            # Make sure there are an even number of values ​​on each line
            if len(assignments) % 2 != 0:
                continue
            
            # Converts each interval to a tuple of two values [(x1, y1), (x2, y2)]
            intervals = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in assignments]
            
            a_start, a_end = intervals[0] # intervals[0] = (x1, y1), a_start = x1, a_end = y1
            b_start, b_end = intervals[1] # intevals[1] = (x2, y2), b_start = x2, b_end = y2
                
            # Check if one interval is completely contained within the other
            if (a_start >= b_start and a_end <= b_end) or (a_start <= b_start and a_end >= b_end):
                count += 1

        return count

if __name__ == "__main__":
    print(totalContainedPairs("input4.txt"))





