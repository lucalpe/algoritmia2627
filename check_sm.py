from os.path import basename, splitext
import sys
import glob
from typing import TextIO

from suma_maxima import Data, Result, read_data, process_rec as process


TEST_DIR = "vectores_sm"


def error(m: str):
    sys.stderr.write(f"Error: {m}\n")
    sys.exit(1)


def abre(n: str) -> TextIO | None :
    try:
        return open(n)
    except:
        error(f"No he podido abrir el fichero {n} para lectura")


def read_solution(f: TextIO) -> Result:
    sum = int(f.readline())
    b = int(f.readline())
    e = int(f.readline())
    return sum, b, e


def check_solution(data: Data, expected: Result, found: Result):
    if expected == found:
        print("OK")
        return
    sume = expected[0]
    sumf, b, e = found
    if sume != sumf:
        print(f"Error: suma incorrecta: {sumf} en lugar de {sume}")
        return
    real = sum(data[b:e])
    if real != sume:
        print(f"Error: el vector encontrado no suma {sume}")
        return
    print("OK")


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
