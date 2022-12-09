def solve(input: str):
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


if __name__ == "__main__":
    input = open("./input/sample_inputs/day_9_sample.txt").read().strip()
    inputMain = open("./input/day9.txt").read().strip()
    solve(input)
    solve(inputMain)
