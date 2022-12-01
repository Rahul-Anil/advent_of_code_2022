def part1(input: str) -> int:
    elves = input.split("\n\n")
    calPerElf = []
    for cal in elves:
        temp = [int(t) for t in cal.split("\n")]
        calPerElf.append(temp)
    x = [sum(c) for c in calPerElf]
    return max(x)


def part2(input: str) -> int:
    elves = input.split("\n\n")
    calPerElf = []
    for cal in elves:
        temp = [int(t) for t in cal.split("\n")]
        calPerElf.append(temp)
    x = [sum(c) for c in calPerElf]
    x.sort(reverse=True)
    return x[0] + x[1] + x[2]


def test():
    print(f"TEST")
    with open("./input/sample_inputs/day_1_sample.txt") as f:
        input = f.read()
    print(f"P1: {part1(input)}")
    assert part1(input) == 24000
    print(f"P2: {part2(input)}")
    assert part2(input) == 45000
    print("\n")


if __name__ == "__main__":
    with open("./input/day1.txt") as f:
        input = f.read()

    test()
    print(f"SOLUTION")
    print(f"P1: {part1(input)}")
    print(f"P2: {part2(input)}")
