o = []
x = 1

for line in open("./input/day10.txt").read().strip().splitlines():
    if line.startswith("noop"):
        o.append(x)
    else:
        v = int(line.strip().split()[1])
        o.append(x)
        o.append(x)
        x += v

# print(f"p1: {sum(x * y for x, y in list(enumerate(o))[20::40])}")

for i in range(0, len(o), 40):
    for j in range(40):
        print("#" if abs(o[i + j] - j) <= 1 else " ", end="")
    print()
