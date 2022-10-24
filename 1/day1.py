def countDeeperValues(depths):
  deeperCount = 0
  previous_measurement = depths[0]
  
  for depth in depths:
    if depth > previous_measurement:
      deeperCount += 1
    previous_measurement = depth

  return deeperCount
  

if __name__ == "__main__":
  # Get depths of input values
  inputData = open("input.txt", "r")
  depths = inputData.readlines()
  depths = [int(d) for d in depths]
  
  # Part 1
  print(countDeeperValues(depths))
  
  # Convert depths to sliding window sums, not allowing partial windows
  sums = []
  for start in range(0, len(depths) - 2):
    sums.append(sum(depths[start:start+3]))
    
  # Part 2
  print(countDeeperValues(sums))