import re

known = set()
beacon_y = set()
Y = 2000000

for line in open(0).read().strip().splitlines():
    sx, sy, bx, by = map(int, re.findall("[0-9]+", line))

    d = abs(sx - bx) + abs(sy - by)
    o = d - abs(sy - Y)

    # print(f"sx: {sx}, sy: {sy}")
    # print(f"bx: {bx}, by: {by}")

    if o < 0:
        continue

    lx = sx - o
    hx = sx + o

    # print(f"lx: {lx}")
    # print(f"hx: {hx}")
    # print()

    if by == Y:
        beacon_y.add(bx)

    for i in range(lx, hx + 1):
        known.add(i)

# print(known)
# print(beacon_y)

known = known - beacon_y
print(len(known))
