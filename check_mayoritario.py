from os.path import basename, splitext
import sys
import glob
from typing import TextIO

from mayoritario import Data, Result, read_data, process


TEST_DIR = "vectores_mayoritario"


def error(m: str):
    sys.stderr.write(f"Error: {m}\n")
    sys.exit(1)


def abre(n: str) -> TextIO | None :
    try:
        return open(n)
    except:
        error(f"No he podido abrir el fichero {n} para lectura")


def read_solution(f: TextIO) -> Result:
    l = f.readline()
    if l == "No hay elemento mayoritario\n":
        return None
    return int(l)


def check_solution(data: Data, expected: Result, found: Result):
    if expected == found:
        print("OK")
        return
    if found is None:
        print(f"No se ha encontrado el elemento mayoritario: {expected}")
        return
    if expected is None:
        print(f"No hay elemento mayoritario pero se ha devuelto: {found}")
        return
    print(f"Se ha devuelto {found} en lugar de {expected}")


def main():
    for vec in sorted(glob.glob(f"{TEST_DIR}/*.vec")):
        name = basename(vec)
        print(name, end= ": ")
        f = open(vec)
        data = read_data(f)
        result = process(data)
        sol = f"{splitext(vec)[0]}.sol"
        f = open(sol)
        expected = read_solution(f)
        check_solution(data, expected, result)

if __name__ == "__main__":
    main()
