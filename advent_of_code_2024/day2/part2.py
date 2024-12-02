from advent_of_code_2024.inputs import load_input


def day2_part2(input: str) -> int:
  reports = parse_input(input)
  safe_reports = 0

  for report in reports:
    safe_reports += 1 if is_safe(report) else 0

  return safe_reports

def parse_input(input: str) -> list[list[int]]:
  raw_reports = input.split("\n")
  reports = []

  for raw_report in raw_reports:
    report = []
    for level in raw_report.split(' '):
      report.append(int(level))
    reports.append(report)

  return reports

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
def is_safe(report: list[int]) -> bool:
  l = 0
  r = 1
  
  if report[l] == report[r]:
    if report[l] == report[r + 1]:
      return False
    else:
      l = 1
      r = 2

  direction = _asc if report[l] < report[r] else _desc
  used_problem_dampener = False
  
  while l < len(report) - 1 and r < len(report):
    is_following_direction = direction(report[l], report[r])
    increase_within_safety = 1 <= abs(report[l] - report[r]) <= 3

    if is_following_direction and increase_within_safety:
      r += 1 if r - l == 1 else 0
      l += 1
      continue

    if not used_problem_dampener:
      used_problem_dampener = True
      r += 1
      continue
    
    return False

  return True

def _asc(a: int, b: int) -> bool:
  return a < b

def _desc(a: int, b: int) -> bool:
  return a > b


if __name__ == "__main__":
  result = day2_part2(load_input(2))
  print(result)