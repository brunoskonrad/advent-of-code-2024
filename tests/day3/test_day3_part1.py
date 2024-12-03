import pytest

from advent_of_code_2024.day3 import part1


@pytest.fixture
def fixture():
  return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def test_input(fixture):
  assert part1.day3_part1(fixture) == 161

def test_parse_input(fixture):
  assert part1.parse_input(fixture) == ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
