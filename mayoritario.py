import sys
from tokenize import endpats
from typing import TextIO, Iterable, Self

from algoritmia.schemes.dac_scheme import IDivideAndConquerProblem, div_solve

type Data = list[int]
type Result = int | None

def read_data(f: TextIO) -> Data:
    lines: list[str] = f.readlines()

    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]

def process__(data: Data) -> Result:
    class MayoritarioProblem(IDivideAndConquerProblem[Result]):
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.size = self.end - self.start

        def is_simple(self) -> bool:
            return self.size <= 1 #len(v) = self.end - self.start

        def trivial_solution(self) -> Result:
            if self.size == 1:
                return v[self.start]
            else:
                return None

        def divide(self) -> Iterable["MayoritarioProblem"]:
            mid = (self.start + self.end) // 2
            yield MayoritarioProblem(self.start, mid)
            yield MayoritarioProblem(mid, self.end)

        def combine(self, solutions: Iterable[Result]) -> Result:
            left_sol, right_sol = solutions
            if left_sol == right_sol:
                return left_sol
            if left_sol is not None:
                cont=0
                for i in range(self.start, self.end):
                    if v[i] == left_sol:
                        cont += 1
                        if cont >= self.size // 2:
                            return left_sol
            if right_sol is not None:
                cont = 0
                for i in range(self.start, self.end):
                    if v[i] == right_sol:
                        cont += 1
                        if cont >= self.size // 2:
                            return right_sol
            return None
    v=data
    mp = MayoritarioProblem(0, len(v))
    return div_solve(mp)

def process(data: Data) -> Result:
    def rec(start: int, end : int) -> Result:
        size = end - start
        if size <= 1:
            if size == 1:
                return v[start]
            else:
                return None
        else:
            mid = (start + end) // 2
            m_left = rec(start, mid)
            m_right = rec(mid, end)
            if m_left == m_right:
                return m_left
            if m_left is not None:
                cont=0
                for i in range(start, end):
                    if v[i] == m_left:
                        cont += 1
                        if cont > size // 2:
                            return m_left
            if m_right is not None:
                cont = 0
                for i in range(start, end):
                    if v[i] == m_right:
                        cont += 1
                        if cont > size // 2:
                            return m_right
            return None

    v = data
    return rec(0, len(v))


def show_result(result: Result):
    print(result)

if __name__ == "__main__":
      data0 = read_data(sys.stdin)
      result0 = process(data0)
      show_result(result0)

