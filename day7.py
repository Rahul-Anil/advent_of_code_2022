import math
import numpy as np
from collections import defaultdict, Counter


def part1(input: str) -> int:
    lines = input.splitlines()

    currDir = None
    prevDir = None

    dirMap = defaultdict(None)  # current: prev
    dirdir = defaultdict(int)

    idx = 0
    while idx < len(lines):
        cl = lines[idx]

        # knowing my curre and prev direc
        if cl[2:4] == "cd":
            if cl[5:] == "/":
                currDir = "root"
                dirMap[currDir] = prevDir
            elif cl[5:] == "..":
                currDir = prevDir
                prevDir = dirMap[currDir]
            else:
                prevDir = currDir
                currDir = cl[5:]
                dirMap[currDir] = prevDir
            idx += 1

        if cl[2:] == "ls":
            idx += 1
            cl = lines[idx]
            while cl[0] != "$":
                if cl[:3] == "dir":
                    dirdir[currDir] += dirdir[cl[4:]]
                else:
                    val = cl.split(" ")[0]
                    dirdir[currDir] += int(val)
                    tempcurr = currDir
                    tempprev = prevDir
                    while dirMap[tempcurr] != None:
                        dirdir[dirMap[tempcurr]] += int(val)
                        tempcurr = tempprev
                        tempprev = dirMap[prevDir]
                idx += 1
                if not idx < len(lines):
                    break
                cl = lines[idx]

    sum = 0
    for d in dirdir.values():
        if d < 100000:
            sum += d

    return sum


def part2(input: str) -> int:
    return 0


def test():
    print(f"TEST")
    with open("./input/sample_inputs/day_7_sample.txt") as f:
        input = f.read()

    print(f"P1: {part1(input)}")
    assert part1(input) == 95437
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
