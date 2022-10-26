import sys
from typing import TextIO


def read_data(f: TextIO) -> tuple[int, list[int]]:
    C = int(f.readline())
    W = [int(linea) for linea in f.readlines()]
    return C, W


def process(C: int, w: list[int]) -> list[int]:
    free: list[int] = C
    contenedores: list[int] = [0] * len(w)
    indices = sorted(range(len(w)),
                     key=lambda i: -W[i])  # Esto ordena los índices para que los pesos estén ordenados por peso, tenemos que repasarlo
    for i in range(len(w)):
        obj = w[i]

    for obj in range(len(free)):
        # Elegir el contenedor
        nc = None
        for c in free[c] >= obj:
            if free[c] >= obj:
                nc = c
                break

        if nc == None:
            free.append(C)
            nc = len(free) - 1

        # Insertar el contenedor
        free[nc] -= obj
        contenedores[i] = nc
    return contenedores


def show_results(contenedores: list[int]):
    for c in contenedores:
        print(c)


if __name__ == "__main__":
    C, W = read_data(sys.stdin)
    contenedores = process(C, W)
    show_results(contenedores)
