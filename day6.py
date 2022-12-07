def part1(input: str) -> int:
    data = input.strip()
    for i in range(0, len(data) - 4):
        tempSet = set(data[i : i + 4])
        if len(tempSet) == 4:
            break

    return i + 4


def part2(input: str) -> int:
    data = input.strip()
    for i in range(0, len(data) - 14):
        tempSet = set(data[i : i + 14])
        if len(tempSet) == 14:
            break

    return i + 14


def test():
    print(f"TEST")
    with open("./input/sample_inputs/day_6_sample.txt") as f:
        input = f.read()

    print(f"P1: {part1(input)}")
    assert part1(input) == 7
    print(f"P2: {part2(input)}")
    assert part2(input) == 19
    print("\n")


if __name__ == "__main__":
    with open("./input/day6.txt") as f:
        input = f.read()

    test()
    print("SOLUTION")
    print(f"P1: {part1(input)}")
    print(f"P2: {part2(input)}")
