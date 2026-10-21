from random import seed

from algoritmia.viewers.labyrinth_viewer import LabyrinthViewer
from shortest_path import process

CELL_SIZE = 15 # Ajustar según la resolución de la pantalla
if __name__ == "__main__":
    rows = int(input("Filas: "))
    cols = int(input("Columnas: "))
    data = (rows, cols)
    labyrinth, path = process(data)
    lv = LabyrinthViewer(labyrinth,
    canvas_width=CELL_SIZE * cols,
    canvas_height=CELL_SIZE * rows)
    lv.add_path(path)
    lv.run()