import sys
from typing import TextIO

def read_data(f: TextIO) -> list[int]:
    lines = f.readlines()
    return [int(line) for line in lines]


def process(data: list[int]) -> bool:
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                return True
    return False
def show_result(result: bool):
    print("No hay repetidos" if not result
            else "Hay repetidos")


if __name__ == "__main__":
    data = read_data(sys.stdin)
    result = process(data)
    show_result(result)