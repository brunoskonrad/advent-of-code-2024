from advent_of_code_2024.inputs import load_input


def solution(input: str) -> str:
    return 0


def parse_input(input: str) -> list[list[str]]:
    return [list(line) for line in input.split("\n")]


if __name__ == "__main__":
    result = solution(load_input(5))
    print(result)
