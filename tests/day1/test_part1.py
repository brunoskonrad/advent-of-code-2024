import pytest
from advent_of_code_2024.day1 import part1


@pytest.fixture
def fixture():
  return '''3   4
4   3
2   5
1   3
3   9
3   3'''


def test_input(fixture):
  assert part1.day1_part1(fixture) == 11

def test_parsing(fixture):
  assert part1.parse_input(fixture) == (
    [3, 4, 2, 1, 3, 3],
    [4, 3, 5, 3, 9, 3],
  )