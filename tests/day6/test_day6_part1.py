import pytest

from advent_of_code_2024.day6 import part1


@pytest.fixture
def fixture():
    return """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_solution(fixture):
    assert part1.solution(fixture) == 41


def parse_input(fixture):
    assert str(part1.parse_input(fixture)) == fixture
