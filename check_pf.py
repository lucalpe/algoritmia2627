from os.path import basename, splitext
import sys
import glob
from typing import TextIO

from punto_fijo import Data, Result, read_data, process


TEST_DIR = "vectores_pf"


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
    if l == "No hay punto fijo\n":
        return None
    return int(l)


def check_solution(data: Data, expected: Result, found: Result):
    if expected == found:
        print("OK")
        return
    if found == None:
        print(f"Error: no se ha encontrado punto fijo y {expected} lo es")
        return
    if 0 <= found < len(data) and data[found] == found:
        print("OK")
        return
    print(f"Error: {found} no es un punto fijo")


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
