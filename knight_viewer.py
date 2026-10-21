from algoritmia.viewers.graph2d_viewer import Graph2dViewer
from knight import knight_graph

CELL_SIZE = 80 # Ajustar según la resolución de la pantalla
if __name__ == "__main__":
    rows = int(input("Filas: "))
    cols = int(input("Columnas: "))

    graph = knight_graph(rows, cols)
    gv = Graph2dViewer(graph,
    canvas_width=CELL_SIZE * cols,
    canvas_height=CELL_SIZE * rows,
    vertexmode=Graph2dViewer.ROW_COL)
    gv.run()