# Para que sea una entrada válida, tiene que estar ordenados y no tiene que tener repetidos.
import sys
from typing import TextIO, Optional


def read_data(f: TextIO) -> list[int]:
    entrada = []
    for line in f.readlines():
        entrada.append(int(line))


# return [int(line) for line in f.readlines()]

def process(entrada: list[int]):
    def pf(i: int, j: int) -> Optional[int]:
        if j <= i:
            return None
        c = (i + j) // 2
        if entrada[c] == c: # Encontrado
            return c
        if entrada[c] < c:
            return pf(c + 1, j)

        if entrada[c] > c:
            return pf(i, c)

    return pf(0, len(entrada))


def show_results(pf: Optional[int]):
    if pf is None:
        print("No hay punto fijo")
    else:
        print(pf)


if __name__ == "__main__":
    entrada = read_data(sys.stdin)
    pf = process(entrada)
    show_results(pf)
