from random import seed

from algoritmia.viewers.labyrinth_viewer import LabyrinthViewer
from df_path import process

CELL_SIZE = 15 # Ajustar según la resolución de la pantalla
if __name__ == "__main__":
    rows = int(input("Filas: "))
    cols = int(input("Columnas: "))
    additional = int(input("Caminos adicionales: "))
    data = (rows, cols, additional)
    labyrinth, path_bf, path_df = process(data)
    lv = LabyrinthViewer(labyrinth,
    canvas_width=CELL_SIZE * cols,
    canvas_height=CELL_SIZE * rows)
    lv.add_path(path_bf)
    lv.add_path(path_df, offset=2, color="blue")
    lv.run()