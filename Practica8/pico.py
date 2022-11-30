import sys
from typing import TextIO

Solution = int

def read_data(f: TextIO) -> list[int]:
    return [int(line) for line in f.readlines()]


def process(v: list[int]) -> Solution:
    def pico(i: int, j: int) -> Solution:
        if j - i == 1:
            return i

        c = (i + j) // 2

        if c == 0:  # vector de dos elementos, tengo que tener cuidado
            if v[c] >= v[1]:
                return 0
            return pico(c+1, j)
        if c == len(v) - 1:
            if v[c] >= v[c - 1]:
                return c
            return pico(i, c)
        if v[c] >= v[c - 1] and v[c] >= v[c + 1]:
            return c
        if v[c+1] >= v[c]:
            return pico(c + 1, j)
        return pico(i, c)
    return pico(0, len(entrada))


def show_results(pico: Solution):
    print(pico)


if __name__ == "__main__":
    entrada = read_data(sys.stdin)
    sol = process(entrada)
    show_results(sol)
