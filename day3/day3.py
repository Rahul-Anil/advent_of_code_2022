import string

letters = list(string.ascii_letters)
priority = {}
s = 1
for l in letters:
    priority[l] = s
    s += 1


def part1(input: str) -> int:
    sack = []
    common = []
    sum = 0
    for rucksack in input.strip().splitlines():
        l = len(rucksack)
        c1, c2 = rucksack[: l // 2], rucksack[l // 2 :]
        sack.append([c1, c2])
        common.append(set(c1) & set(c2))

    for i in common:
        for l in i:
            sum += priority[l]

    return sum


def part2(input: str) -> int:
    sack = []
    common = []
    sum = 0

    for rucksack in input.strip().splitlines():
        sack.append(rucksack)

    for i in range(0, len(sack), 3):
        p = set(sack[i]) & set(sack[i + 1]) & set(sack[i + 2])
        p = list(p)
        sum += priority[p[0]]

    return sum


def test():
    print(f"TEST")
    with open("./input/sample_inputs/day_3_sample.txt") as f:
        input = f.read()

    print(f"P1: {part1(input)}")
    assert part1(input) == 157
    print(f"P2: {part2(input)}")
    assert part2(input) == 70
    print("\n")


if __name__ == "__main__":
    with open("./input/day3.txt") as f:
        input = f.read()

    test()
    print("SOLUTION")
    print(f"P1: {part1(input)}")
    print(f"P2: {part2(input)}")
