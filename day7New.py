from collections import defaultdict


def part1(input: str) -> int:
    lines = input.splitlines()
    currDir = prevDir = None
    dirMap = defaultdict(None)
    dir = defaultdict(list)

    while idx < len(lines):
        c = lines[idx]

        if c[0] == "$":
            if c[2] == "c":
                d = c[5:]
                if d == "/":
                    currDir = "root"
                    dirMap[currDir] = prevDir
                elif d == "..":
                    cd
    return 0


def part2(input: str) -> int:
    return 0


def test():
    print(f"TEST")
    with open("./input/sample_inputs/day_7_sample.txt") as f:
        input = f.read()

    print(f"P1: {part1(input)}")
    assert part1(input) == 0
    print(f"P2: {part2(input)}")
    assert part2(input) == 0
    print("\n")


if __name__ == "__main__":
    with open("./input/day7.txt") as f:
        input = f.read()

    test()
    print("SOLUTION")
    print(f"P1: {part1(input)}")
    # print(f"P2: {part2(input)}")
