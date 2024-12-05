import pytest

from advent_of_code_2024.day2 import part1


@pytest.fixture
def fixture():
    return """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_input(fixture):
    assert part1.day2_part1(fixture) == 2


def test_parse_input(fixture):
    assert part1.parse_input(fixture) == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_is_safe_when_decreasing():
    assert part1.is_safe([7, 6, 4, 2, 1]) == True


def test_is_safe_when_increasing():
    assert part1.is_safe([1, 3, 6, 7, 9]) == True


def test_is_unsafe_when_increasing_by_more_than_three():
    assert part1.is_safe([1, 2, 7, 8, 9]) == False


def test_is_unsafe_when_decreasing_by_more_than_three():
    assert part1.is_safe([9, 7, 6, 2, 1]) == False


def test_is_unsafe_when_levels_increase_and_decrease():
    assert part1.is_safe([1, 3, 2, 4, 5]) == False


def test_is_unsafe_when_neither_increasing_nor_decreasing():
    assert part1.is_safe([8, 6, 4, 4, 1]) == False
