"""easier way to do this would have been to just type the crates in"""


def part1(input: str) -> int:
    # print(f"input: {input}")
    crates, order = input.split("\n\n")

    moves = []  # (number, from , to)

    for o in order.splitlines():
        temp = o.split(" ")
        moves.append((int(temp[1]), int(temp[3]), int(temp[5])))

    crates = crates.splitlines()
    newCrates = []
    for c in crates:
        newCrates.append(c)

    crate = [[] for c in range(9)]

    for i in range(7, -1, -1):
        for j in range(1, 34, 4):
            crateNum = (j - 1) // 4
            c = newCrates[i][j]
            # print(f"c: {c}, i:{i}, j:{j}")
            if c != " ":
                crate[crateNum].append(c)

    for m in moves:
        number, f, t = m
        for i in range(number):
            crate[t - 1].append(crate[f - 1].pop())

    for c in crate:
        print(c.pop(), end="")

    print("")
    return 0


def part2(input: str) -> int:
    # print(f"input: {input}")
    crates, order = input.split("\n\n")

    moves = []  # (number, from , to)

    for o in order.splitlines():
        temp = o.split(" ")
        moves.append((int(temp[1]), int(temp[3]), int(temp[5])))

    crates = crates.splitlines()
    newCrates = []
    for c in crates:
        newCrates.append(c)

    crate = [[] for c in range(9)]

    for i in range(7, -1, -1):
        for j in range(1, 34, 4):
            crateNum = (j - 1) // 4
            c = newCrates[i][j]
            # print(f"c: {c}, i:{i}, j:{j}")
            if c != " ":
                crate[crateNum].append(c)

    # print(crate)

    for m in moves:
        num, f, t = m
        f = f - 1
        t = t - 1
        tomove = crate[f][-num:]  # get values that we need to move
        crate[f] = crate[f][:-num]  # remove end values form frm array
        crate[t] = crate[t] + tomove  # add the new elements to the new array

    for c in crate:
        print(c.pop(), end="")

    print("")
    return 0


def test():
    print(f"TEST")
    with open("./input/sample_inputs/day_5_sample.txt") as f:
        input = f.read()

    # print(f"P1: {part1(input)}")
    # assert part1(input) == 0
    print(f"P2: {part2(input)}")
    assert part2(input) == 0
    print("\n")


if __name__ == "__main__":
    with open("./input/day5.txt") as f:
        input = f.read()

    # test()
    print("SOLUTION")
    print(f"P1: {part1(input)}")
    print(f"P2: {part2(input)}")
