#!/usr/bin/env python3
import sys
from typing import TextIO

type Data = list[int]
type Result = int

def read_data(f: TextIO) -> Data:
    # Leer del fichero f
    lines = f.readlines()
    return [int(line) for line in lines]


def process(data: list[int]) -> int:
    numeros: dict[int, int] = {}
    for num in data:
        numeros[num] = numeros.get(num, 0) + 1

    return max(numeros, key=numeros.get)

def show_result(result: Result):
    # Escribir el resultado
    print(result)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)