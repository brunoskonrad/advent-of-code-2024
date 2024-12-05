import pytest

from advent_of_code_2024.day4 import part2


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
    assert part2.solution(fixture) == 9
