def isAdj(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def solve1(input):
    hx, hy = 0, 0
    tx, ty = 0, 0
    visited = set()
    for line in input.strip().splitlines():
        direction, steps = line.strip().split()
        for _ in range(int(steps)):
            if direction == "R":
                hy += 1
            elif direction == "L":
                hy -= 1
            elif direction == "U":
                hx += 1
            elif direction == "D":
                hx -= 1

            if not isAdj(hx, hy, tx, ty):
                sx = 0 if hx == tx else (hx - tx) / abs(hx - tx)
                sy = 0 if hy == ty else (hy - ty) / abs(hy - ty)

                tx += sx
                ty += sy
                # print(f"tx: {tx}, ty: {ty}")

            visited.add((tx, ty))
    print(f"count: {len(visited)}")


def solve2(input: str):
    visited = set()
    knot = [[0, 0] for _ in range(10)]
    for line in input.strip().splitlines():
        direction, steps = line.strip().split()
        for _ in range(int(steps)):
            if direction == "R":
                knot[0][1] += 1
            elif direction == "L":
                knot[0][1] -= 1
            elif direction == "U":
                knot[0][0] += 1
            elif direction == "D":
                knot[0][0] -= 1

            for k in range(1, 10):
                hx, hy = knot[k - 1]
                tx, ty = knot[k]

                if not isAdj(hx, hy, tx, ty):
                    sx = 0 if hx == tx else (hx - tx) / abs(hx - tx)
                    sy = 0 if hy == ty else (hy - ty) / abs(hy - ty)

                    tx += sx
                    ty += sy

                    knot[k] = [tx, ty]

            visited.add(tuple(knot[9]))
    print(f"count: {len(visited)}")


if __name__ == "__main__":
    input1 = open("./input/sample_inputs/day_9_sample1.txt").read().strip()
    input2 = open("./input/sample_inputs/day_9_sample.txt").read().strip()
    inputMain = open("./input/day9.txt").read().strip()
    solve1(input1)
    solve1(inputMain)
    solve2(input2)
    solve2(inputMain)
