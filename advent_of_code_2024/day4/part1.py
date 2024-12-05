from advent_of_code_2024.inputs import load_input

PUZZLE_WORD = "XMAS"


def day4_part1(input: str) -> str:
    puzzle = parse_input(input)

    counter = 0

    for x, line in enumerate(puzzle):
        for y, char in enumerate(line):
            if char == "X":
                if has_word_horizontal(puzzle, x, y):
                    counter += 1
                if has_word_horizontal_backwards(puzzle, x, y):
                    counter += 1
                if has_word_vertical(puzzle, x, y):
                    counter += 1
                if has_word_vertical_backwards(puzzle, x, y):
                    counter += 1
                if has_word_diagonal_top_right(puzzle, x, y):
                    counter += 1
                if has_word_diagonal_top_left(puzzle, x, y):
                    counter += 1
                if has_word_diagonal_bottom_left(puzzle, x, y):
                    counter += 1
                if has_word_diagonal_bottom_right(puzzle, x, y):
                    counter += 1

    return counter


def has_word_horizontal(puzzle: list[list[str]], x: int, y: int) -> bool:
    try:
        return (
            puzzle[x][y + 1] == "M"
            and puzzle[x][y + 2] == "A"
            and puzzle[x][y + 3] == "S"
        )
    except Exception:
        return False


def has_word_horizontal_backwards(puzzle: list[list[str]], x: int, y: int) -> bool:
    if y - 3 < 0:
        return False

    try:
        return (
            puzzle[x][y - 1] == "M"
            and puzzle[x][y - 2] == "A"
            and puzzle[x][y - 3] == "S"
        )
    except Exception:
        return False


def has_word_vertical(puzzle: list[list[str]], x: int, y: int) -> bool:
    try:
        return (
            puzzle[x + 1][y] == "M"
            and puzzle[x + 2][y] == "A"
            and puzzle[x + 3][y] == "S"
        )
    except Exception:
        return False


def has_word_vertical_backwards(puzzle: list[list[str]], x: int, y: int) -> bool:
    if x - 3 < 0:
        return False

    try:
        return (
            puzzle[x - 1][y] == "M"
            and puzzle[x - 2][y] == "A"
            and puzzle[x - 3][y] == "S"
        )
    except Exception:
        return False


def has_word_diagonal_top_right(puzzle: list[list[str]], x: int, y: int) -> bool:
    try:
        return (
            puzzle[x + 1][y + 1] == "M"
            and puzzle[x + 2][y + 2] == "A"
            and puzzle[x + 3][y + 3] == "S"
        )
    except Exception:
        return False


def has_word_diagonal_top_left(puzzle: list[list[str]], x: int, y: int) -> bool:
    if y - 3 < 0:
        return False

    try:
        return (
            puzzle[x + 1][y - 1] == "M"
            and puzzle[x + 2][y - 2] == "A"
            and puzzle[x + 3][y - 3] == "S"
        )
    except Exception:
        return False


def has_word_diagonal_bottom_left(puzzle: list[list[str]], x: int, y: int) -> bool:
    if x - 3 < 0 or y - 3 < 0:
        return False

    try:
        return (
            puzzle[x - 1][y - 1] == "M"
            and puzzle[x - 2][y - 2] == "A"
            and puzzle[x - 3][y - 3] == "S"
        )
    except Exception:
        return False


def has_word_diagonal_bottom_right(puzzle: list[list[str]], x: int, y: int) -> bool:
    if x - 3 < 0:
        return False

    try:
        return (
            puzzle[x - 1][y + 1] == "M"
            and puzzle[x - 2][y + 2] == "A"
            and puzzle[x - 3][y + 3] == "S"
        )
    except Exception:
        return False


def parse_input(input: str) -> list[list[str]]:
    return [list(line) for line in input.split("\n")]


if __name__ == "__main__":
    result = day4_part1(load_input(4))
    print(result)
