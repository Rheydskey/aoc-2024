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
    e1 = l1.pop()
    r += l2.count(e1) * e1

print(r)
