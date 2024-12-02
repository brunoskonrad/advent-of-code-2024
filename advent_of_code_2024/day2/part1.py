from advent_of_code_2024.inputs import load_input

# Lines per input
reports = None

# list of numbers per report
levels = []

def day2_part1(input: str) -> int:
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
  if report[0] == report[1]:
    return False

  direction = _asc if report[0] < report[1] else _desc
  
  i = 0
  while i < len(report) - 1:
    if not direction(report[i], report[i+1]):
      return False
    
    if not 1 <= abs(report[i] - report[i+1]) <= 3:
      return False

    i += 1

  return True

def _asc(a: int, b: int) -> bool:
  return a < b

def _desc(a: int, b: int) -> bool:
  return a > b


if __name__ == "__main__":
  result = day2_part1(load_input(2))
  print(result)