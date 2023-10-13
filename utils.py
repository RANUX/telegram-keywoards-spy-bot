from typing import List

def read_file_lines(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]
