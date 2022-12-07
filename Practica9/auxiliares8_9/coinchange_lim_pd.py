from typing import Optional
import sys


infinity = float("infinity")

Solution = tuple[int, list[int]]


def read_data(f) -> tuple[int, int, list[int], list[int], list[int]]:
    N = int(f.readline())
    Q = int(f.readline())
    v = [int(w) for w in f.readline().split()]
    w = [int(w) for w in f.readline().split()]
    m = [int(w) for w in f.readline().split()]
    return N, Q, v, w, m


def process(impl: int, N: int, Q: int, v: list[int], w: list[int], m: list[int]) -> Solution:
    if impl == 0:
        return coinchange_direct(N, Q, v, w, m)
    elif impl == 1:
        return coinchange_memo(N, Q, v, w, m)
    elif impl == 2:
        return coinchange_memo_path(N, Q, v, w, m)
    elif impl == 3:
        return coinchange_iter(N, Q, v, w, m)
    elif impl == 4:
        return coinchange_iter_red(N, Q, v, w, m)


def coinchange_direct(N: int, Q: int, v: list[int], w: list[int], m: list[int]) -> Solution:
    raise NotImplementedError("coinchange_direct")


def coinchange_memo(N: int, Q: int, v: list[int], w: list[int], m: list[int]) -> Solution:
    raise NotImplementedError("coinchange_memo")


def coinchange_memo_path(N: int, Q: int, v: list[int], w: list[int], m: list[int]) -> Solution:
    raise NotImplementedError("coinchange_memo_path")


def coinchange_iter(N: int, Q: int, v: list[int], w: list[int], m: list[int]) -> Solution:
    raise NotImplementedError("coinchange_iter")


def coinchange_iter_red(N: int, Q: int, v: list[int], w: list[int], m: list[int]) -> Solution:
    raise NotImplementedError("coinchange_iter_red")


def show_results(s: int, ds: Optional[list[int]]):
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
