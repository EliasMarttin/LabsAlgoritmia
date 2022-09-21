import sys
from typing import TextIO

def read_data(f: TextIO) -> list[int]:
    lines = f.readlines()
    return [int(line) for line in lines]


def show_results(nums: list[int]):
    for num in nums:
        print(num)


if __name__ == "__main__":
    nums = read_data(sys.stdin)
    show_results(nums)