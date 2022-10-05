import sys
from random import shuffle
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet


def read_data(f: TextIO) -> tuple[int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols


def process(rows: int, cols: int) -> UndirectedGraph:
    vertices = []
    corridors = []
    for i in range(rows):
        for j in range(cols):
            vertices.append((i, j))

    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)
    edges = []

    for r,c in vertices:
        if r+1 < rows:
            edges.append(((r,c),(r+1,c)))
        if c+1 < cols:
            edges.append(((r,c),(r,c+1)))

    shuffle(edges)
    for u,v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))

    return UndirectedGraph(E = corridors)


def show_results(labyrinth: UndirectedGraph):
    print(labyrinth)


if __name__ == "__main__":
    rows, cols = read_data(sys.stdin)
    labyrinth = process(rows, cols)
    show_results(labyrinth)
