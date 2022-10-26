import sys
from typing import TextIO
from collections.abc import Iterator, Iterable
from dataclasses import dataclass
from algoritmia.schemes.bt_scheme import DecisionSequence, bt_solve, Solution
from sudoku_lib import Sudoku, primera_vacia, posibles_en, desde_cadenas, pretty_print, vacias


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


def process_avanzado(sudoku: Sudoku) -> Iterator[Sudoku]:
    @dataclass
    class Extra:
        sudoku: Sudoku
        vacias = set[Position]

    class sudokuDS(DecisionSequence):
        def is_solution(self) -> bool:
            return primera_vacia(self.extra.sudoku) is None

        def solution(self) -> Solution:
            return self.extra.sudoku

        def successors(self) -> Iterable["DecisionSequence"]:
            pos = None
            best = 10
            for v in self.extra.vacias:
                p = len(posibles_en(self.extra.sudoku, v))
                if p < best:
                    best = p
                    pos = v
            if pos is not None:
                copia = [fila[:] for fila in self.extra.sudoku]
                copia_vacias = self.extra.vacias - {pos}
                for n in posibles_en(copia, pos):
                    copia[pos[0]][pos[1]] = n

            v = set(vacias(sudoku))
            yield self.add_decision(n, Extra(copia, copia_vacias))

    yield from bt_solve(sudokuDS(Extra(sudoku)))


if (__name__) == "__name__":
    sudoku = read_data(sys.stdin)
    solutions = process(sudoku)
    show_results(sudoku)
