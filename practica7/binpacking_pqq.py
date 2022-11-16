import sys
from collections.abc import Iterable
from dataclasses import dataclass
from typing import TextIO
from algoritmia.schemes.bab_scheme import BoundedDecisionSequence, bab_max_solve, Score, bab_min_solve, Solution


def read_data(f: TextIO) -> tuple[int, list[int]]:
    C = int(f.readline())
    W = [int(linea) for linea in f.readlines()]
    return C, W


def process(C: int, w: list[int]) -> list[int]:
    @dataclass
    class Extra:
        free: list[int]

    class BinpackingDS(BoundedDecisionSequence):
        def calculate_opt_bound(self) -> Score:
            minObjeto = w[-1]
            libre = sum(f for f in self.extra.free if f >= minObjeto)
            maxHueco = max(self.extra.free)
            caben = 0
            total = 0
            for i in range(len(self),C):
                if w[i] <= maxHueco:
                    caben += w[i]
            nuevos = (total - min(caben, libre) + C-1) // C
            return len(self.extra.free) + nuevos

        def calculate_pes_bound(self) -> Score:
            pass

        def is_solution(self) -> bool:
            return len(self) == C

        def solution(self) -> Solution:
            return list(self.decisions())

        def successors(self) -> Iterable["DecisionSequence"]:
             if not self.is_solution():
                obj = w[len(self)]
                for i in range(len(self.extra.free)):
                    if obj <= self.extra.free[i]: # cabe
                        free_copia = self.extra.free[:]
                        free_copia [i] -= obj
                        yield self.add_decision(i+1, free_copia)
                free_copia = self.extra.free[:]
                free_copia[i] -= obj
                yield self.add_decision(i + 1, free_copia)
    return bab_min_solve(BinpackingDS)


def process_old(C: int, w: list[int]) -> list[int]:
    free: list[int] = C
    contenedores: list[int] = []
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
        contenedores.append(nc)
    return contenedores


def show_results(contenedores: list[int]):
    for c in contenedores:
        print(c)


if __name__ == "__main__":
    C, W = read_data(sys.stdin)
    contenedores = process(C, W)
    show_results(contenedores)
