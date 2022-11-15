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
  
def binary_to_decimal(bin):
  result = 0
  for idx, digit in enumerate(bin[::-1]): # Reverse iterate
    result += int(digit) * 2**idx
  return result

if __name__ == "__main__":
    # Get input
    input_data = open("input.txt", "r")
    numbers = input_data.readlines()
    numbers = [n.strip() for n in numbers]
    
    print(get_power(numbers))