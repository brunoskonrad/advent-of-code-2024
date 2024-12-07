from enum import Enum
from typing import Union

from typing_extensions import Self

from advent_of_code_2024.inputs import load_input


def solution(input: str) -> int:
    map = parse_input(input)
    map.run()
    return sum(isinstance(value, TraversedStep) for value in map.grid.values())


def parse_input(input: str):
    lines = input.split("\n")

    width = len(lines)
    height = len(lines[0])

    map = Map(width, height)

    for x, line in enumerate(lines):
        for y, character in enumerate(line):
            if character == "#":
                map.set(Point(x, y), Obstacle())
            if character == "^":
                point = Point(x, y)
                guard = Guard(point)

                map.set(point, guard)

    return map


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add(self, p: Self) -> Self:
        return Point(self.x + p.x, self.y + p.y)

    def __str__(self):
        return f"{self.x},{self.y}"


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Guard:
    def __init__(self, position: Point):
        self.direction = Direction.UP
        self.position = position

    @property
    def move_vector(self) -> Point:
        if self.direction == Direction.UP:
            return Point(-1, 0)
        if self.direction == Direction.RIGHT:
            return Point(0, 1)
        if self.direction == Direction.DOWN:
            return Point(1, 0)
        if self.direction == Direction.LEFT:
            return Point(0, -1)

    def rotate(self):
        if self.direction == Direction.UP:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.UP

    def __str__(self):
        if self.direction == Direction.UP:
            return "^"
        if self.direction == Direction.RIGHT:
            return ">"
        if self.direction == Direction.DOWN:
            return "V"
        if self.direction == Direction.LEFT:
            return "<"


class Obstacle:
    def __str__(self):
        return "#"


class TraversedStep:
    def __str__(self):
        return "X"


class Map:
    guard: Guard
    grid: dict[str, Union["Guard", "Obstacle", "TraversedStep"]]

    def __init__(self, width: int, height: int):
        self.grid = {}
        self.width = width
        self.height = height

    def run(self):
        if self.guard:
            while self.is_inside_the_map(self.guard.position):
                desired_position = self.guard.move_vector.add(self.guard.position)

                if self.can_move_to(desired_position):
                    self.set(self.guard.position, TraversedStep())
                    self.set(desired_position, self.guard)
                    self.guard.position = desired_position
                else:
                    self.guard.rotate()

    def set(self, p: Point, v: Union["Guard", "Obstacle", "TraversedStep"]):
        self.grid[str(p)] = v

        if isinstance(v, Guard):
            self.guard = v

    def get(self, p: Point) -> Union["Guard", "Obstacle", "TraversedStep", None]:
        return self.grid.get(str(p), None)

    def can_move_to(self, p: Point) -> bool:
        return not isinstance(self.get(p), Obstacle)

    def is_inside_the_map(self, p: Point) -> bool:
        return p.x > 0 and p.x < self.width and p.y > 0 and p.y < self.height

    def __str__(self):
        lines = []
        for x in range(0, self.width):
            characters = []
            for y in range(0, self.height):
                point = self.get(Point(x, y))
                if point:
                    characters.append(str(point))
                else:
                    characters.append(".")
            lines.append("".join(characters))

        return "\n".join(lines)


if __name__ == "__main__":
    result = solution(load_input(6))
    print(result)
