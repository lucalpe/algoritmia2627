import sys
from typing import TextIO, Self

from algoritmia.schemes.dac_scheme import IDecreaseAndConquerProblem, dec_solve

type Data = list[int]
type Result = int | None

def read_data(f: TextIO) -> Data:
    # Transformamos cada línea en un entero:
    return [int(line) for line in f.readlines()]

def process(data: Data) -> Result:
    class PuntoFijoProblem(IDecreaseAndConquerProblem[Result]):
        def __init__(self, start, end):
            self.start: int = start
            self.end: int = end
            self.size = self.end - self.start

        def is_simple(self) -> bool:
            return self.size <= 1

        def trivial_solution(self) -> Result:
            return self.start

        def decrease(self) -> Self:
            pass

    v = data
    sm = PuntoFijoProblem(0, len(v))
    return dec_solve(sm)

def show_result(result: Result):
    print(result)

if __name__ == "__main__":
    data0 = read_data(sys.stdin)
    result0 = process(data0)
    show_result(result0)
