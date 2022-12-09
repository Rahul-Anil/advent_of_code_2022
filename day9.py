def solve1(input: str):
    visited = set()
    hx, hy, tx, ty = 0, 0, 0, 0
    for line in input.strip().split("\n"):
        direction, step = line.strip().split()
        for _ in range(int(step)):
            if direction == "R":
                hy += 1
            elif direction == "L":
                hy -= 1
            elif direction == "U":
                hx += 1
            elif direction == "D":
                hx -= 1

            if (max(abs(hx - tx), abs(hy - ty))) > 1:
                if hx - tx == 0:
                    tx += 0
                elif hx - tx <= -1:
                    tx += -1
                else:
                    tx += 1
                if hy - ty == 0:
                    ty += 0
                elif hy - ty <= -1:
                    ty += -1
                else:
                    ty += 1

            visited.add((tx, ty))

    print(f"count: {len(visited)}")
    pass


def solve2(input: str):
    knotMoves = {
        (0, 2): (0, 1),
        (0, -2): (0, -1),
        (2, 0): (1, 0),
        (-2, 0): (-1, 0),
        (1, 2): (1, 1),
        (-1, 2): (-1, 1),
        (1, -2): (1, -1),
        (-1, -2): (-1, -1),
        (2, 1): (1, 1),
        (2, -1): (1, -1),
        (-2, 1): (-1, 1),
        (-2, -1): (-1, -1),
        (2, 2): (1, 1),
        (2, -2): (1, -1),
        (-2, 2): (-1, 1),
        (-2, -2): (-1, -1),
    }
    visited = set()
    knotPos = [(0, 0) for _ in range(10)]
    for line in input.strip().splitlines():
        print(line)
        direction, steps = line.strip().split()
        for _ in range(int(steps)):
            if direction == "U":
                knotPos[0] = (knotPos[0][0], knotPos[0][1] + 1)
            elif direction == "D":
                knotPos[0] = (knotPos[0][0], knotPos[0][1] - 1)
            elif direction == "L":
                knotPos[0] = (knotPos[0][0] - 1, knotPos[0][1])
            elif direction == "R":
                knotPos[0] = (knotPos[0][0] + 1, knotPos[0][1])
            for i in range(1, 10):
                if (
                    max(
                        abs(knotPos[i - 1][0] - knotPos[i][0]),
                        abs(knotPos[i - 1][1] - knotPos[i][1]),
                    )
                    > 1
                ):
                    key = (
                        knotPos[i - 1][0] - knotPos[i][0],
                        knotPos[i - 1][1] - knotPos[i][1],
                    )
                    knotPos[i] = (
                        knotPos[i][0] + knotMoves[key][0],
                        knotPos[i][1] + knotMoves[key][1],
                    )
            visited.add(knotPos[9])
    print(len(visited))


if __name__ == "__main__":
    input = open("./input/sample_inputs/day_9_sample.txt").read().strip()
    inputMain = open("./input/day9.txt").read().strip()
    solve2(input)
    solve2(inputMain)
