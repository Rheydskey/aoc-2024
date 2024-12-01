l1 = []
l2 = []

while True:
    try:
        line = input()
        e1, e2 = line.split()
        l1.append(int(e1))
        l2.append(int(e2))
    except EOFError:
        print(l1, l2)
        break

l1.sort(reverse=True)
l2.sort(reverse=True)

r = 0
while len(l1) != 0 and len(l2) != 0:
    min_l1 = l1.pop()
    min_l2 = l2.pop()
    r += max(min_l1 - min_l2, min_l2 - min_l1)

print(r)
