import sys
from random import seed
from typing import TextIO

from algoritmia.algorithms.shortest_path import path_recover
from algoritmia.algorithms.traverse import traverse_bf, traverse_df
from algoritmia.datastructures.graphs import UndirectedGraph

from problemas.sesion_1_2.create_labyrinth import create_labyrinth

type Vertex = tuple[int, int]
type Edge = tuple[Vertex, Vertex]
type Path = list[Vertex]
type Data = tuple[int, int, int]
type Result = tuple[UndirectedGraph[Vertex], Path, Path]

def read_data(f: TextIO) -> Data:
    rows = int(f.readline())
    cols = int(f.readline())
    additional = int(f.readline())
    return rows, cols, additional

def process(data: Data) -> Result:
    f, c, a = data
    laberinto = create_labyrinth(f, c, n=a)
    camino_bf = path_recover(traverse_bf(laberinto, (0,0)), (f-1, c-1))
    camino_df = path_recover(traverse_df(laberinto, (0,0)), (f-1, c-1))

    return laberinto, camino_bf, camino_df

def show_result(result: Result):
    laberinto, camino1, camino2 = result
    print(laberinto)
    print(camino1)
    print("-------------------------------------------------------------------------------------------")
    print(camino2)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)