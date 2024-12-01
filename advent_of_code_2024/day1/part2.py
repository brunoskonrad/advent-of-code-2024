from advent_of_code_2024.inputs import load_input


def day1_part2(input: str) -> int: 
  (left, right) = parse_input(input)
  occurrances = count_occurrances(right)
  
  total_distance = 0

  for item in left:
    total_distance += item * occurrances.get(str(item), 0)

  return total_distance


def parse_input(input: str) -> tuple[list[int], list[int]]:
  lines = input.split('\n')

  left = []
  right = []

  for line in lines:
    entries = line.split('   ')
    left.append(int(entries[0]))
    right.append(int(entries[1]))

  return (left, right)


def count_occurrances(array: list[int]) -> dict[int, int]:
  occurrances = {}

  for i in array:
    k = str(i)
    if k not in occurrances:
      occurrances[k] = 0
    occurrances[k] += 1

  return occurrances


if __name__ == "__main__":
  result = day1_part2(load_input(1))
  print(result)