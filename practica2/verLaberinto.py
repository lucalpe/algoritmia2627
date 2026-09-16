from algoritmia.viewers.labyrinth_viewer import LabyrinthViewer
from labyrinth import process

CELL_SIZE = 20 # Ajustar según la resolución de la pantalla
if __name__ == "__main__":
    rows = int(input("Filas: "))
    cols = int(input("Columnas: "))
    data = (rows, cols)
    labyrinth = process(data)
    lv = LabyrinthViewer(labyrinth,
    canvas_width=CELL_SIZE * cols,
    canvas_height=CELL_SIZE * rows)
    lv.run()