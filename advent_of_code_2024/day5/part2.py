import math
from functools import cmp_to_key

from advent_of_code_2024.inputs import load_input


def solution(input: str) -> int:
    page_ordering_rules, pages_to_produce = parse_input(input)
    comparator = PageOrderingComparator(page_ordering_rules)

    total = 0

    for page_to_produce in pages_to_produce:
        if not page_to_produce.is_valid(page_ordering_rules):
            page_to_produce.sort(comparator)
            total += page_to_produce.middle

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

    def has_page(self, page: int) -> bool:
        return self.pages.get(page, None) is not None

    def has_page_sequences(self, x: int, y: int) -> bool:
        return self.has_page(x) and y in self.pages.get(x)


class PageOrderingComparator:
    def __init__(self, page_order_rules: PageOrderingRules):
        self.page_order_rules = page_order_rules

    def compare(self, x: int, y: int) -> int:
        if self.page_order_rules.has_page_sequences(x, y):
            return 1

        if self.page_order_rules.has_page_sequences(y, x):
            return -1

        return 0


class PagesToProduce:
    pages: list[int]

    def __init__(self, pages):
        self.pages = pages

    def is_valid(self, page_ordering_rules: PageOrderingRules) -> bool:
        for x, y in zip(self.pages, self.pages[1:]):
            if not page_ordering_rules.is_valid(x, y):
                return False
        return True

    def sort(self, comparator: PageOrderingComparator):
        self.pages = sorted(
            self.pages, key=cmp_to_key(comparator.compare), reverse=True
        )

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
