# def part1(input: str) -> int:
#     elves = input.split("\n\n").join("")
#     calPerElf = []
#     for cal in elves:
#         temp = [int(t) for t in cal.split("\n")]
#         calPerElf.append(temp)
#     x = [sum(c) for c in calPerElf]
#     return max(x)


def part1(input: str) -> int:
    C = []
    for elf in input.split("\n\n"):
        c = 0
        for cal in elf.split("\n"):
            c += int(cal)
        C.append(c)
    return max(C)


def part2(input: str) -> int:
    C = []
    for elf in input.split("\n\n"):
        c = 0
        for cal in elf.split("\n"):
            c += int(cal)
        C.append(c)
    C.sort(reverse=True)
    return sum(C[:3])


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
