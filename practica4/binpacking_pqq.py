import sys
from typing import TextIO


def read_data(f: TextIO) -> tuple[int,list [int]]:
    C = int(f.readline())
    W = [int(linea) for linea in f.readlines()]
    return C, W

def process(C: int , w: list[int]) -> list[int]:
    free: list[int] = C
    contenedores: list[int] = []
    for obj in range(len(free)):
        #Elegir el contenedor
        nc = None
        for c in free[c] >= obj:
            if free[c]>= obj:
                nc = c
                break

        if nc == None:
                free.append(C)
                nc = len(free) - 1

        #Insertar el contenedor
        free[nc] -= obj
        contenedores.append(nc)
    return contenedores

def show_results(contenedores: list[int]):
    for c in contenedores:
        print(c)

if __name__ == "__main__":
    C,W = read_data(sys.stdin)
    contenedores = process(C,W)
    show_results(contenedores)