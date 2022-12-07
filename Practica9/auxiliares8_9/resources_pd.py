from typing import Optional
import sys

Vector = list[int]
Matrix = list[list[int]]
Solution = tuple[int, Optional[Vector]]

Score = int
Decision = int
SParams = tuple[int, int]

Mem = dict[SParams, Score]
MemPath = dict[SParams, tuple[Score, SParams, Decision]]


def read_data(f) -> tuple[int, int, Vector, Matrix]:
    U = int(f.readline())
    N = int(f.readline())
    m = [int(w) for w in f.readline().split()]
    v = [[int(w) for w in l.split()] for l in f.readlines()]
    return U, N, m, v


def process(impl: int, U: int, N: int, m: Vector, v: Matrix) -> Solution:
    if impl == 0:
        return resources_direct(U, N, m, v)
    elif impl == 1:
        return resources_memo(U, N, m, v)
    elif impl == 2:
        return resources_memo_path(U, N, m, v)
    elif impl == 3:
        return resources_iter(U, N, m, v)
    elif impl == 4:
        return resources_iter_red(U, N, m, v)


def resources_direct(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    def S(u: int, n: int) -> int:
        if n == 0:
            return 0
        if n > 0:
            ms = 0
            for d in range(min(m[n - 1], u) + 1):
                s = S(u - d, n - 1) + v[n - 1][d]
                if s > ms:
                    ms = s
            return ms

        # return max(S(u-d, n-1) + v[n-1][d]   Esto es lo mismo de arriba per más corto
        #            for d in range(min(m[n-1], u) + 1))

    return S(U, N), None


def resources_memo(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    def S(u: int, n: int) -> int:
        if n == 0:
            return 0
        if n > 0:
            if (u, n) not in mem:
                mem[u, n] = max(S(u - d, n - 1) + v[n - 1][d]
                                for d in range(min(m[n - 1], u) + 1))
                return mem[u, n]

    mem: Mem = {}
    return S(U, N), None


def resources_memo_path(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    def S(u: int, n: int) -> int:
        if n == 0:
            return 0
        if n > 0:
            if (u, n) not in mem:
                mem[u, n] = max((S(u - d, n - 1) + v[n - 1][d],
                                 (u - d, n - 1),
                                 d)
                                for d in range(min(m[n - 1], u) + 1)
                                )
            return mem[u, n][0]

    mem: Mem = {}
    score = S(U, N)
    path = []
    u, n = U, N
    while n > 0:
        _, (u, n), d = mem[u, n]
        path.append(d)

    path.reverse()
    return score, path


def resources_iter(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    raise NotImplementedError("resources_iter")


def resources_iter_red(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    raise NotImplementedError("resources_iter_red")


def show_results(s: int, ds: Optional[Vector]):
    print(s)
    if ds is not None:
        for d in ds:
            print(d)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        impl = 0
    else:
        impl = int(sys.argv[1])
    data = read_data(sys.stdin)
    sol = process(impl, *data)
    show_results(*sol)
