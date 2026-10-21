import sys
from typing import TextIO

from algoritmia.algorithms.traverse import traverse_bf
from algoritmia.datastructures.graphs import UndirectedGraph

type Vertex = tuple[int, int]
type Edge = tuple[Vertex, Vertex]
type Data = tuple[int, int, int, int]
type Result = tuple[UndirectedGraph[Vertex], int]

def knight_graph(rows: int, cols: int) -> UndirectedGraph[Vertex]:
    vertices = [(row, column) for row in range(rows) for column in range(cols)]
    all_edges = []
    for row, col in vertices:
        for ir, ic in [(-2, 1), (-1, 2), (1,2) , (2,1)]:
            if 0 <= row + ir < rows and 0 <= col + ic < cols:
                all_edges.append(((row, col), (row + ir, col + ic)))

    return UndirectedGraph(V=vertices, E=all_edges)

def read_data(f: TextIO) -> Data:
    rows = int(f.readline())
    cols = int(f.readline())
    first_row = int(f.readline())
    first_col = int(f.readline())
    return rows, cols, first_row, first_col

def process(data: Data) -> Result:
    rows, cols, fRow, fCol = data
    grafo = knight_graph(rows, cols)
    lista = list(traverse_bf(grafo, (fRow, fCol)))
    return grafo, len(lista)

def show_result(result: Result):
    laberinto, casillas = result
    print(laberinto)
    print(casillas)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)