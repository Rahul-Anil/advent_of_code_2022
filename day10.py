def solve(input: str):
    cycle = 1
    ss = 0
    tv = 1
    x = []
    check = [20, 60, 100, 140, 180, 220]
    for line in input.strip().splitlines():

        if line.startswith("addx"):
            c, v = line.strip().split()
            v = int(v)
            for _ in range(2):
                if cycle in check:
                    ss += cycle * tv
                    # print(f"cycle: {cycle}, tv: {tv}, ss: {cycle*tv}")
                cycle += 1
            # print(f"v: {v}")
            tv += v

        else:
            if cycle in check:
                ss += cycle * tv
            cycle += 1
    print(f"ss: {ss}")


crt = ["."] * 240
cycle = 0
x = 1


def update_cycle():
    global cycle
    if abs((cycle % 40) - x) <= 1:
        crt[cycle] = "#"
    cycle += 1


def solve2(input: str):
    global x
    for lines in input.strip().splitlines():
        op = lines.split(" ")
        if len(op) == 1:
            update_cycle()
        else:
            update_cycle()
            update_cycle()
            x += int(op[1])

    print("\n".join("".join(crt[r : r + 40]) for r in range(0, 201, 40)))


if __name__ == "__main__":
    input = open("./input/sample_inputs/day_10_sample.txt").read().strip()
    inputMain = open("./input/day10.txt").read().strip()
    # solve2(input)
    solve2(inputMain)
