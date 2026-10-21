from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

from random import shuffle


type Vertex = tuple[int, int]
type Edge = tuple[Vertex, Vertex]


def create_labyrinth(rows: int, cols: int, n:int=0) -> UndirectedGraph[Vertex]:
    vertices: list[Vertex] = [(row, col) for row in range(rows) for col in range(cols)]
    mfs: MergeFindSet[Vertex] = MergeFindSet()
    for v in vertices:
        mfs.add(v)
    all_edges:list[Edge] = [((row, col), (row + 1, col)) for row in range(rows - 1) for col in range(cols)]
    all_edges.extend([((row, col), (row, col + 1)) for row in range(rows) for col in range(cols - 1)])
    shuffle(all_edges)
    corridors:list[Edge] = []
    for (u, v) in all_edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
        elif n > 0:
            n -= 1
            corridors.append((u, v))
    return UndirectedGraph(E=corridors)
