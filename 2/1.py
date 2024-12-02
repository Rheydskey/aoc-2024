def is_safe(l: list[int]) -> bool:
    is_decreasing = all(i > j for i, j in zip(l, l[1:]))
    is_increasing = all(i < j for i, j in zip(l, l[1:]))
    safe = all(1 <= abs(i - j) <= 3 for i, j in zip(l, l[1:]))
    return safe and (is_decreasing or is_increasing)


with open("1", "r") as f:
    print([is_safe([int(li) for li in line.strip().split()]) for line in f.readlines()].count(True))
