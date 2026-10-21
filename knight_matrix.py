import sys
from itertools import count
from typing import TextIO

from algoritmia.algorithms.shortest_path import path_recover, shortest_path_unweighted_graph
from algoritmia.algorithms.traverse import traverse_bf

from knight import knight_graph

type Vertex = tuple[int, int]
type Matrix = list[list[int]]
type Data = tuple[int, int]
type Result = Matrix


def read_data(f: TextIO) -> Data:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols


def process(data: Data) -> Result:
    rows, cols = data
    grafo = knight_graph(rows, cols)
    matriz = [[-1 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            camino = shortest_path_unweighted_graph(grafo, (0,0), (r, c))
            matriz[r][c] = len(camino) - 1

    return matriz

def show_result(result: Result):
    for row in result:
        print(' '.join(str(e) for e in row))

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)