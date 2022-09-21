from typing import TextIO
import sys

def read_data(f: TextIO) -> list[int]:
    lines = f.readlines()
    return [int(line) for line in lines]



def process(nums: list[int]) -> int:
        m = nums[0]
        for num in nums:
            if num < m:
                m = num
        return m

def show_results(m: int):
        print(m)

if __name__ == "__main__":
    nums = read_data(sys.stdin)
    m = process(nums)
    show_results(m)