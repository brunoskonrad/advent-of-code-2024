import os


def load_input(day: int) -> str:
  input_file = os.path.join(os.path.dirname(__file__), f"day_{day}.txt")
  with open(input_file, encoding="utf-8") as f:
    return f.read().strip()
