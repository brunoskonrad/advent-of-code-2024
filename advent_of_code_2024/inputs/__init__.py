import os


def load_input(day: int) -> str:
  input_file = os.path.join(os.path.dirname(__file__), f"day_{day}.txt")
  f = open(input_file, "r", encoding="utf-8")
  return f.read().strip()
