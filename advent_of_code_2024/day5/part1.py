import math

from advent_of_code_2024.inputs import load_input


def solution(input: str) -> str:
    page_ordering_rules, pages_to_produce = parse_input(input)

    total = 0

    for page in pages_to_produce:
        if page.is_valid(page_ordering_rules):
            total += page.middle

    return total


class PageOrderingRules:
    _raw_pages: list[str]
    pages: dict[int, set[int]]

    def __init__(self, pages: list[str]):
        self._raw_pages = pages
        self.pages = {}

        for line in self._raw_pages.split("\n"):
            x, y = line.split("|")
            x, y = int(x), int(y)

            if x not in self.pages:
                self.pages[x] = set()
            self.pages[x].add(y)

    def is_valid(self, x: int, y: int) -> bool:
        return self.pages.get(x, None) and y in self.pages[x]


class PagesToProduce:
    pages: list[int]

    def __init__(self, pages):
        self.pages = pages

    def is_valid(self, page_ordering_rules: PageOrderingRules) -> bool:
        for x, y in zip(self.pages, self.pages[1:]):
            if not page_ordering_rules.is_valid(x, y):
                return False
        return True

    @property
    def middle(self) -> int:
        index = math.ceil((len(self.pages) - 1) / 2)
        return self.pages[index]


def parse_pages_to_produce(input: str) -> list[PagesToProduce]:
    pages_to_produce = []

    for input_line in input.split("\n"):
        line = []
        for item in input_line.split(","):
            line.append(int(item))
        pages_to_produce.append(PagesToProduce(line))

    return pages_to_produce


def parse_input(input: str) -> tuple[PageOrderingRules, list[PagesToProduce]]:
    page_ordering_rules, pages_to_produce = input.split("\n\n")
    return PageOrderingRules(page_ordering_rules), parse_pages_to_produce(
        pages_to_produce
    )


if __name__ == "__main__":
    result = solution(load_input(5))
    print(result)
