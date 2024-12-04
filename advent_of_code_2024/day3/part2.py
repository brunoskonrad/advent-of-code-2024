import re

from advent_of_code_2024.inputs import load_input


def day3_part1(input: str) -> str:
  instructions = parse_input(input)
  doing = True
  result = 0

  for instruction in instructions:
    if instruction.startswith("don't"):
      doing = False
      continue

    if instruction.startswith("do"):
      doing = True
      continue

    if not doing:
      continue

    numbers = re.search(r"\((\d{1,3}),(\d{1,3})\)", instruction)

    if numbers:
      a, b = int(numbers.group(1)), int(numbers.group(2))
      result += a * b

  return result

def parse_input(input: str) -> list[str]:
  return re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", input)

def flatten(xss):
  return [x for xs in xss for x in xs]

if __name__ == "__main__":
  result = day3_part1(load_input(3))
  print(result)