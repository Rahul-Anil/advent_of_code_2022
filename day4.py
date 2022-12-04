def part1(input: str) -> int:
    count = 0
    for pair in input.splitlines():
        e1, e2 = pair.split(",")
        e1l, e1u = e1.split("-")
        e2l, e2u = e2.split("-")
        e1l, e1u = int(e1l), int(e1u)
        e2l, e2u = int(e2l), int(e2u)

        s1 = set(range(e1l, e1u + 1))
        s2 = set(range(e2l, e2u + 1))

        l = len(s1 & s2)

        if l == len(s1) or l == len(s2):
            count += 1

    return count


def part2(input: str) -> int:
    count = 0
    for pair in input.splitlines():
        e1, e2 = pair.split(",")
        e1l, e1u = e1.split("-")
        e2l, e2u = e2.split("-")
        e1l, e1u = int(e1l), int(e1u)
        e2l, e2u = int(e2l), int(e2u)

        s1 = set(range(e1l, e1u + 1))
        s2 = set(range(e2l, e2u + 1))

        l = len(s1 & s2)

        if l > 0:
            count += 1

    return count


def test():
    print(f"TEST")
    with open("./input/sample_inputs/day_4_sample.txt") as f:
        input = f.read()

    print(f"P1: {part1(input)}")
    assert part1(input) == 2
    print(f"P2: {part2(input)}")
    assert part2(input) == 4
    print("\n")


if __name__ == "__main__":
    with open("./input/day4.txt") as f:
        input = f.read()

    test()
    print("SOLUTION")
    print(f"P1: {part1(input)}")
    print(f"P2: {part2(input)}")
