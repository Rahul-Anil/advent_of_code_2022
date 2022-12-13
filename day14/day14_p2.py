b = set()
abyss = 0

for line in open(0).read().strip().splitlines():
    x = [list(map(int, p.split(","))) for p in line.split(" ->")]
    for (x1, y1), (x2, y2) in zip(x, x[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                b.add((x, y))
                abyss = max(abyss, y)

abyss += 1
t = 0
while (500, 0) not in b:
    sx, sy = (500, 0)
    while sy < abyss:
        if (sx, sy + 1) not in b:
            sx, sy = sx, sy + 1
        elif (sx - 1, sy + 1) not in b:
            sx, sy = sx - 1, sy + 1
        elif (sx + 1, sy + 1) not in b:
            sx, sy = sx + 1, sy + 1
        else:
            break
        continue
    # print(f"sx:{sx} , sy:{sy}")
    b.add((sx, sy))
    t += 1

print(t)
