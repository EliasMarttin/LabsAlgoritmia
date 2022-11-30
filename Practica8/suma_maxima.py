import sys
from typing import TextIO

Solution = tuple[int, int, int]

def read_data(f: TextIO) -> list[int]:
    return [int(line) for line in f.readlines()]


def process(v: list[int]) -> Solution:
    def sm(i: int, j: int) -> Solution:
        if j - i == 1:  # Caso base.
            return v[i], i, j
        c = (i + j) // 2
        sol_iz = sm(i, c)
        sol_der = sm(c + 1, j)
        sum_der = 0
        ac = 0
        in_der = c + 1
        for k in range(c + 1, j):
            ac += v[k]
            if ac > sum_der:
                sum_der = ac
                in_der = k + 1

        sum_izq = 0
        ac = 0
        in_izq = c + 1  # importante esto, para no incluir ese elemento
        for k in range(c, i - 1):  # Como es range, para incluir el 0, se añade sumando uno o en este caso restando.
            ac += v[k]
            if ac > sum_der:
                sum_izq = ac
                in_izq = k

        sol_centro = (sum_der + sum_izq, in_izq, in_der)
        return max(sol_iz, sol_der, sol_centro)  # En caso de empate, hay que ver que nos dicen.

    return sm(0, len(v))


def show_results(sol: Solution):
    print(sol[0])
    print(sol[1])
    print(sol[2])


if __name__ == "__main__":
    entrada = read_data(sys.stdin)
    sol = process(entrada)
    show_results(sol)
