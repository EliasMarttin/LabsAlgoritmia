import sys
from typing import TextIO
from collections.abc import Iterator, Iterable
from dataclasses import dataclass
from algoritmia.schemes.bt_scheme import DecisionSequence, bt_solve, Solution
from sudoku_lib import Sudoku, primera_vacia, posibles_en, desde_cadenas, pretty_print


def read_data(f: TextIO) -> Sudoku:
     return desde_cadenas(f.readlines())
def show_results(sudoku: Iterator[Sudoku]):
    for sudoku in sudoku:
        pretty_print(sudoku)

def process(sudoku: Sudoku) -> Iterator[Sudoku]:
    @dataclass
    class Extra:
        sudoku: Sudoku

    class sudokuDS(DecisionSequence):
        def is_solution(self) -> bool:
            return primera_vacia(self.extra.sudoku) is None

        def solution(self) -> Solution:
            return self.extra.sudoku

        def successors(self) -> Iterable["DecisionSequence"]:
            pos = primera_vacia(self.extra.sudoku)
            if pos is not None:
                copia = [fila[:] for fila in self.extra.sudoku]
                for n in posibles_en(copia, pos):
                    copia[pos[0]][pos[1]] = n

            yield self.add_decision(n, Extra(copia))

    yield from bt_solve(sudokuDS(Extra(sudoku)))
if(__name__) == "__name__":
    sudoku = read_data(sys.stdin)
    solutions = process(sudoku)
    show_results(sudoku)