def part1(input: str) -> int:
    print(f"input: {input}")
    return 0


def part2(input: str) -> int:
    return 0


def test():
    print(f"TEST")
    with open("./input/sample_inputs/day_6_sample.txt") as f:
        input = f.read()

    print(f"P1: {part1(input)}")
    assert part1(input) == 0
    print(f"P2: {part2(input)}")
    assert part2(input) == 0
    print("\n")


if __name__ == "__main__":
    with open("./input/day6.txt") as f:
        input = f.read()

    test()
    print("SOLUTION")
    # print(f"P1: {part1(input)}")
    # print(f"P2: {part2(input)}")
