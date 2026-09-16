import sys
from random import shuffle, random, seed
from typing import TextIO
from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

type Vertex = tuple[int, int]
# (row, col)
type Edge = tuple[Vertex, Vertex]
type Data = tuple[int, int]
# (n_rows, n_cols)
type Result = UndirectedGraph[Vertex]

def read_data(f: TextIO) -> Data:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols
def process(data: Data) -> Result:
    # Paso 1
    rows, cols = data
    vertices = [(row, column) for row in range(rows) for column in range(cols)]

    # Paso 2
    mfs = MergeFindSet()
    for vertice in vertices:
        mfs.add(vertice)

    # Paso 3
    all_edges = []
    for row, col in vertices:
        if row + 1 < rows:
            all_edges.append(((row, col), (row + 1, col)))
        if col + 1 < cols:
            all_edges.append(((row, col), (row, col + 1)))
    shuffle(all_edges)

    # Paso 4
    corridors = []

    # Paso 5
    a_d_c = 200
    for v1, v2 in all_edges:
        if mfs.find(v1) != mfs.find(v2):
            mfs.merge(v1, v2)
            corridors.append((v1, v2))
        else:
            if a_d_c > 0:
                corridors.append((v1, v2))
                a_d_c -= 1

    return UndirectedGraph(E = corridors)

def show_result(result: Result):
    print(result)

if __name__ == "__main__":
    seed(65)
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)