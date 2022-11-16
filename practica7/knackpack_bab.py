import sys
from collections.abc import Iterable
from dataclasses import dataclass
from typing import TextIO

from algoritmia.schemes.bab_scheme import BoundedDecisionSequence, bab_max_solve

Weight = int
Value = int
Solution = tuple[Value, Weight, tuple[int, ...]]
Score = int
State = tuple[int, Weight]

def read_data(f: TextIO) -> tuple[int, list[Value], list[Weight]]:
    W = int(f.readline())
    v = []
    w = []
    for line in f.readlines():
        elems = line.strip().split()
        v.append(int(elems[0]))
        w.append(int(elems[1]))

    return W, v, w


@dataclass
class Extra:
    acum : Weight
    value: Value

def process(W: int, v: list[Value], w: list[Weight]) -> tuple[Value, Weight, tuple[int, ...]]:

    class KnapsakDS(BoundedDecisionSequence):
        def is_solution(self) -> bool:
            return len(self) == len(v) #tomaré una decision por cada elemento.

        def solution(self) -> Solution:
            return self.extra.value, self.extra.acum, self.decisions()

        def successors(self) -> Iterable["KnapsakDS"]:
            if len(self) < len(W):  # if not.is_solution():
                if self.extra.acum + w[len(self)] <= W:
                    new_accum = self.extra.acc_sum + w[len(self)]
                    yield self.add_decision(1, Extra(new_accum, self.extra.value + v[len(self)]))
                yield self.add_decision(0, self.extra)

        def calculate_opt_bound(self) -> Score:
            value = self.extra
            free = w - self.extra.acum
            for i in range(len(self), n):
                if w[i] <= free:
                    value += v[i]
                    free -= w[i]

                else:
                    r = free / w[i]
                    value += r * v[i]
                    break
            return value
        def calculate_pes_bound(self) -> Score:

            value = self.extra
            free = w - self.extra.acum
            for i in range(len(self), n):
                if w[i] <= free:
                    value += v[i]
                    free -= w[i]

            return value




    n = len(w)
    return bab_max_solve(KnapsakDS(Extra(0, 0)))

def show_results(sol: Solution):
    print(sol[0])
    print(sol[1])
    for d in sol[2]:
        print(d)

if __name__ == "__main__":
    W,v,w = read_data(sys.stdin)
    sol = process(W,v,w)
    show_results(sol)