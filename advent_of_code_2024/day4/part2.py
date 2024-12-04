from advent_of_code_2024.inputs import load_input


def solution(input: str) -> str:
  puzzle = parse_input(input)

  counter = 0

  for x, line in enumerate(puzzle):
    for y, char in enumerate(line):
      if char == 'A' and check(puzzle, x, y):
        counter += 1

  return counter

VALID_ENTRIES = [
  ['M', 'M', 'S', 'S'],
  ['M', 'S', 'M', 'S'],
  ['S', 'M', 'S', 'M'],
  ['S', 'S', 'M', 'M'],
]


def check(puzzle: list[list[str]], x: int, y: int) -> bool:
  out_bounds_x = (0 == x or x == len(puzzle) - 1)
  out_bounds_y = (0 == y or y == len(puzzle[y]) - 1)
  
  if out_bounds_x or out_bounds_y:
    return False
  
  top_left = puzzle[x-1][y-1]
  top_right = puzzle[x-1][y+1]
  bottom_left = puzzle[x+1][y-1]
  bottom_right = puzzle[x+1][y+1]

  return [top_left, top_right, bottom_left, bottom_right] in VALID_ENTRIES

def parse_input(input: str) -> list[list[str]]:
  return [list(line) for line in input.split('\n')]

if __name__ == "__main__":
  result = solution(load_input(4))
  print(result)