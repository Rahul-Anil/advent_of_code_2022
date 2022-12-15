import re


lines = [list(map(int, re.findall("[0-9]+", line))) for line in open(0)]

Y = 10
intervals = []
beacon_y = set()

for line in lines:
    sx, sy, bx, by = line

    d = abs(sx - bx) + abs(sy - by)
    o = d - abs(sy - Y)

    if o < 0:
        continue

    lx = sx - o
    hx = sx + o

    intervals.append((lx, hx))

    if by == Y:
        beacon_y.add(bx)

intervals.sort()

print(intervals)
q = []

for lo, hi in intervals:
    if not q:
        q.append([lo, hi])
        continue

    qlo, qhi = q[-1]

    if lo > qhi + 1:
        q.append([lo, hi])
        continue

    q[-1][1] = max(qhi, hi)

print(q)

unknown = set()

for lo, hi in q:
    for i in range(lo, hi + 1):
        unknown.add(i)

print(len(unknown - beacon_y))
