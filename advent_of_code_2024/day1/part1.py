from advent_of_code_2024.inputs import load_input

def parse_input(input: str) -> tuple[list[int], list[int]]:
  lines = input.split('\n')

  left = []
  right = []

  for line in lines:
    entries = line.split('   ')
    left.append(int(entries[0]))
    right.append(int(entries[1]))

  return (left, right)

def day1_part1(input: str) -> int: 
  (left, right) = parse_input(input)
  
  left.sort()
  right.sort()

  total_distance = 0

  for item in zip(left, right):
    total_distance += abs(item[0] - item[1])

  return total_distance

if __name__ == "__main__":
  result = day1_part1(load_input(1))
  print(result)