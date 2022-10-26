
from typing import TextIO
from sudoku_lib import Sudoku
from dataclasses import dataclass
from algoritmia.schemes.bt_scheme import DesisionSequence

def read_data(f: TextIO)-> Sudoku:
    pass
def process(sudoku: Sudoku) -> Itetator[Sudoku]:
    @dataClass
    class Extra:
        sudoku: sudoku

    class sudokuDS(DecisionSequence):
        pass

    yield from bt_solve(SudokuDS(Extra(sudoku)))