def binary_to_decimal(bin):
  result = 0
  for idx, digit in enumerate(bin[::-1]): # Reverse iterate
    result += int(digit) * 2**idx
  return result

def get_power(numbers):
  # Count the zeros at each position
  digits = len(numbers[0])
  zeros = [0]*digits
  
  for number in numbers:
    for idx, value in enumerate(number):
      zeros[idx] += int(value == '0')
      
  # Determine most and least common values
  gamma = ''
  epsilon = ''
  half_count = len(numbers) // 2 # integer division
  for count in zeros:
    # Zero is the most common
    if count > half_count:
      gamma += '0'
      epsilon += '1'
    else:
      gamma += '1'
      epsilon += '0'
  
  gamma = binary_to_decimal(gamma)
  epsilon = binary_to_decimal(epsilon)
  return gamma*epsilon
  
def bitwise_criteria(numbers, bit_index, criteria):
  """
  Given a list of numbers, an index, and a function, criteria, which takes the number of 0s and 
  the number of 1s and returns which bit should be kept (true for 1, false for 0).
  """
  if len(numbers) == 1:
    return numbers[0]
  
  # Filter the lists based on the given bit index
  ones = [n for n in numbers if n[bit_index] == '1']
  zeros = [n for n in numbers if n[bit_index] == '0']

  if criteria(len(ones), len(zeros)):
    return bitwise_criteria(ones, bit_index+1, criteria)
  else:
    return bitwise_criteria(zeros, bit_index+1, criteria)

if __name__ == "__main__":
    # Get input
    input_data = open("input.txt", "r")
    numbers = input_data.readlines()
    numbers = [n.strip() for n in numbers]
    
    # Part 1
    print(get_power(numbers))
    
    # Part 2
    oxygen_generator_rating = bitwise_criteria(numbers, 0, lambda ones, zeros: ones >= zeros)
    co2_scrubber_rating = bitwise_criteria(numbers, 0, lambda ones, zeros: zeros > ones)
    print(binary_to_decimal(oxygen_generator_rating) * binary_to_decimal(co2_scrubber_rating))