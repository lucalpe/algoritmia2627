import sys
from random import shuffle, random, seed
from typing import TextIO, Iterator

from algoritmia.algorithms.traverse import traverse_df
from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

type Vertex = tuple[int, int]
# (row, col)
type Edge = tuple[Vertex, Vertex]
type Data = tuple[int, int]
# (n_rows, n_cols)
type Result = UndirectedGraph[Vertex]

def random_df[T](graph: UndirectedGraph[T]) -> Iterator[Edge]:
    def traverse_from(u: T, v: T) -> Iterator[Edge]:
        seen.add(v)
        yield u, v
        s = list(graph.succs(v))
        shuffle(s)
        for suc_v in s:
            if suc_v not in seen:
                yield from traverse_from(v, suc_v)

    seen: set[T] = set()
    return traverse_from((0,0), (0,0))  # Arista fantasma inicial


def read_data(f: TextIO) -> Data:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols

def process(data: Data) -> Result:
    # Paso 1 Creamos todos los vertices posibles a partir de las filas y columnas iniciales
    rows, cols = data
    vertices = [(row, column) for row in range(rows) for column in range(cols)]
    # Paso 3 Creamos todos los edges posibles.
    # Lo hacemos creando vertices entre el vertice actual y el de la derecha y el de abajo
    all_edges = []
    for row, col in vertices:
        if row + 1 < rows:
            all_edges.append(((row, col), (row + 1, col)))
        if col + 1 < cols:
            all_edges.append(((row, col), (row, col + 1)))
    complete = UndirectedGraph(E=all_edges)
    corridors = random_df(complete)
    return UndirectedGraph(E=list(corridors))

def show_result(result: Result):
    print(result)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)