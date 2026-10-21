import sys

from algoritmia.algorithms.shortest_path import path_recover
from algoritmia.algorithms.traverse import traverse_bf
from algoritmia.viewers.labyrinth_viewer import LabyrinthViewer

from labyrinth_df import process

CELL_SIZE = 7 # Ajustar según la resolución de la pantalla
if __name__ == "__main__":
    sys.setrecursionlimit(100000000)

    rows = int(input("Filas: "))
    cols = int(input("Columnas: "))
    data = (rows, cols)
    labyrinth = process(data)
    lv = LabyrinthViewer(labyrinth,
    canvas_width=CELL_SIZE * cols,
    canvas_height=CELL_SIZE * rows)
    edges= traverse_bf(labyrinth, (0,0))
    path = path_recover(edges, (rows-1, cols -1))
    lv.add_path(path)
    lv.run()