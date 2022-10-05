import sys
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from Practica2.labyrinth import create_labyrinth

Vertex = tuple [int,int]
Edge = tuple [Vertex,Vertex]

def bf_search(graph: UndirectedGraph[Vertex],source: Vertex, target: Vertex) -> list[Edge]:
    queue = Fifo()
    seen: set[Vertex] = set()
    seen.add(source)
    queue.push(source)
    res = [(source,source)] #Se suele poner esto para poner la arista ficticia
    while(len(queue))>0:
        v = queue.pop()
        if v == target:
            return res
        for suc in graph.succs(v):
            if suc not in seen:
                queue.push(suc)
                res.append((v,suc))
                seen.add(suc)


    raise Exception ("Imposible") #Se lanza una excepcion  pero también se le puede poner un return


def path_recover(edges: list[Edge], target: Vertex ) -> list[Vertex]:
    bp = {}
    for o,d in edges:
        bp [d]=o
        if d == target:
            break
    path = [target]
    v= target
    while v != bp[v]:
        v = bp[v]
        path.append(v)

    path.reverse()
    return path


def read_data(f: TextIO)-> tuple[int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols

def process(rows: int, cols : int ):
    g = create_labyrinth(rows,cols)
    edges = bf_search(g, (0, 0), (rows-1, cols-1))
    return g, path_recover(edges, (rows-1, cols-1))

def show_results(path: list[Vertex]):
    print(path)

if __name__ == "__main__":
    rows, cols = read_data(sys.stdin)
    g, path = process(rows, cols)
    show_results(path)