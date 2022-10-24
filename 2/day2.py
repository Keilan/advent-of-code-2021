def computePosition(commands):
  distance = 0
  depth = 0
  
  for command in commands:
    direction, amount = command.split()
    amount = int(amount)
    
    # Adjust based on direction, remember that up decreases your depth
    if direction == "forward":
      distance += amount
    if direction == "up":
      depth -= amount
    if direction == "down":
      depth += amount
  
  return distance, depth


def computePosition2(commands):
  distance = 0
  depth = 0
  aim = 0
  
  for command in commands:
    direction, amount = command.split()
    amount = int(amount)
    
    # Adjust based on direction, remember that up decreases your depth
    if direction == "forward":
      distance += amount
      depth += amount*aim
    if direction == "up":
      aim -= amount
    if direction == "down":
      aim += amount
  
  return distance, depth
  

if __name__ == "__main__":
  # Get commands
  inputData = open("input.txt", "r")
  commands = inputData.readlines()
  
  # Part 1
  distance, depth = computePosition(commands)
  print(distance, depth, distance*depth)
  
  # Part 2
  distance, depth = computePosition2(commands)
  print(distance, depth, distance*depth)