import pytest

from advent_of_code_2024.day4 import part1


@pytest.fixture
def fixture():
  return """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def test_input(fixture):
  assert part1.day4_part1(fixture) == 18
