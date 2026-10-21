import sys
from tokenize import endpats
from typing import TextIO, Iterable, Self

from algoritmia.schemes.dac_scheme import IDivideAndConquerProblem, div_solve

type Data = list[int]
type Result = tuple[int, int, int]

def read_data(f: TextIO) -> Data:
    # Transformamos cada línea en un entero:
    return [int(line) for line in f.readlines()]

def process_schema(data: Data) -> Result:
    class SumaMaximaProblem(IDivideAndConquerProblem[Result]):
        def __init__(self, start, end):
            self.start: int = start
            self.end: int = end
            self.size = self.end - self.start

        def is_simple(self) -> bool:
            return self.size <= 1 #len(v) = self.end - self.start

        def trivial_solution(self) -> Result:
            if self.size == 1:
                return (v[self.start], self.start, self.end)
            else:
                return None

        def divide(self) -> Iterable["SumaMaximaProblem"]:
            mid = (self.start + self.end) // 2
            yield SumaMaximaProblem(self.start, mid)
            yield SumaMaximaProblem(mid, self.end)

        def combine(self, solutions: Iterable[Result]) -> Result:
            left_sol, right_sol = solutions
            mid = (self.start + self.end) // 2

            suma_left = 0
            suma = 0
            best_left = 0
            for i in reversed(range(self.start, mid)):
                suma += v[i]
                if suma > suma_left:
                    suma_left = suma
                    best_left = i

            suma_right = 0
            suma = 0
            best_right = 0
            for i in range(mid, self.end):
                suma += v[i]
                if suma > suma_right:
                    suma_right = suma
                    best_right = i + 1
            mid_sol = ((suma_right + suma_left), best_left, best_right)
            return max(left_sol, right_sol, mid_sol)
    v = data
    sm = SumaMaximaProblem(0, len(v))
    return div_solve(sm)

def process_rec(data: Data) -> Result:
    def rec(start: int, end: int) -> Result:
        size = end - start
        if size <= 1:
            return (v[start], start, end)
        else:
            mid = (start + end) // 2
            m_left = rec(start, mid)
            m_right = rec(mid, end)
            suma_left = 0
            suma = 0
            best_left = 0
            for i in reversed(range(start, mid)):
                suma += v[i]
                if suma > suma_left:
                    suma_left = suma
                    best_left = i

            suma_right = 0
            suma = 0
            best_right = 0
            for i in range(mid, end):
                suma += v[i]
                if suma > suma_right:
                    suma_right = suma
                    best_right = i + 1
            mid_sol = ((suma_right + suma_left), best_left, best_right)
            return max(m_left, m_right, mid_sol)
    v = data
    return rec(0, len(v))

def show_result(result: Result):
    print(result)

if __name__ == "__main__":
      data0 = read_data(sys.stdin)
      result0 = process_schema(data0)
      show_result(result0)

