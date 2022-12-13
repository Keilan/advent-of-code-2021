# Converts vents from the input string format to lists giving x1, y1, x2, y2
def parse_vents(vents):
    result = []
    for vent in vents:
        start, end = vent.strip().split(" -> ")
        
        # Get list of ints from start and end coordinates
        values = start.split(',')
        values.extend(end.split(','))
        result.append([int(v) for v in values])
    return result
        
def draw_map(vents):
    # Get max dimension
    max_coordinate = 0
    for v in vents:
        max_coordinate = max(max_coordinate, max(v))
    n = max_coordinate
    
    # Create empty map
    map = [[0]*(n+1) for _ in range(n+1)]
    
    # Add vents
    for x1, y1, x2, y2 in vents:
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        if x1 == x2:
            for y in range(y1, y2+1):
                map[x1][y] += 1
        elif y1 == y2:
            for x in range(x1, x2+1):
                map[x][y1] += 1
        else:
            pass # Skip diagonal line
    
    return map
    
def print_map(map):
    for row in map:
        print_string = ""
        for pos in row:
            print_string += str(pos)
        print(print_string)
  

if __name__ == "__main__":
    # Get vents
    input_data = open("input.txt", "r")
    vents = parse_vents(input_data.readlines())
    
    # Compute the map
    map = draw_map(vents)
    
    # Count values greater than 1
    count = 0
    for row in map:
        count += len([x for x in row if x > 1])
    print(count)