from copy import deepcopy


def is_safe(l: list[int]) -> bool:
    is_decreasing = all(i > j for i, j in zip(l, l[1:]))
    is_increasing = all(i < j for i, j in zip(l, l[1:]))
    safe = all(1 <= abs(i - j) <= 3 for i, j in zip(l, l[1:]))
    return safe and (is_decreasing or is_increasing)


def try_hard(l) -> bool:
    if is_safe(l):
        return True

    d = []
    for i in range(len(l)):
        dc = deepcopy(l)
        dc.pop(i)
        d.append(is_safe(dc))

    return any(d)


with open("1", "r") as f:
    print([try_hard([int(li) for li in line.strip().split()]) for line in f.readlines()].count(True))
