import pytest

from advent_of_code_2024.day1 import part2


@pytest.fixture
def fixture():
    return """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_input(fixture):
    assert part2.day1_part2(fixture) == 31


def test_parsing(fixture):
    assert part2.parse_input(fixture) == (
        [3, 4, 2, 1, 3, 3],
        [4, 3, 5, 3, 9, 3],
    )


def test_occurrances():
    fixture = [4, 3, 5, 3, 9, 3]

    assert part2.count_occurrances(fixture) == {
        "3": 3,
        "4": 1,
        "5": 1,
        "9": 1,
    }
