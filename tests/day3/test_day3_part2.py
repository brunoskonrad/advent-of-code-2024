import pytest

from advent_of_code_2024.day3 import part2


@pytest.fixture
def fixture():
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_input(fixture):
    assert part2.day3_part1(fixture) == 48


def test_parse_input(fixture):
    assert part2.parse_input(fixture) == [
        "mul(2,4)",
        "don't()",
        "mul(5,5)",
        "mul(11,8)",
        "do()",
        "mul(8,5)",
    ]
