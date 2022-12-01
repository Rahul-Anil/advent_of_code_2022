rps = {"A": ["Y", "X", "Z"], "B": ["Z", "Y", "X"], "C": ["X", "Z", "Y"]}

rps2 = {"A": ["B", "A", "C"], "B": ["C", "B", "A"], "C": ["A", "C", "B"]}

rpsScore = {"X": 1, "Y": 2, "Z": 3}
rpsScore2 = {"A": 1, "B": 2, "C": 3}


def part1(input: str) -> int:
    janken = []
    for round in input.strip().split("\n"):
        p1, p2 = round.split(" ")
        janken.append((p1, p2))

    totalScore = 0
    for j in janken:
        roundScore = 0
        p1, p2 = j
        # win
        if rps[p1][0] == p2:
            roundScore += 6 + rpsScore[p2]
        # draw
        if rps[p1][1] == p2:
            roundScore += 3 + rpsScore[p2]

        if rps[p1][2] == p2:
            roundScore += 0 + rpsScore[p2]

        totalScore += roundScore

    # print(totalScore)

    return totalScore


def part2(input: str) -> int:
    janken = []
    for round in input.strip().split("\n"):
        p1, p2 = round.split(" ")
        janken.append((p1, p2))

    totalScore = 0
    for j in janken:
        roundScore = 0
        p1, p2 = j

        # loose
        if p2 == "X":
            roundScore += 0 + rpsScore2[rps2[p1][2]]

        # draw
        if p2 == "Y":
            roundScore += 3 + rpsScore2[rps2[p1][1]]

        # win
        if p2 == "Z":
            roundScore += 6 + rpsScore2[rps2[p1][0]]

        totalScore += roundScore

    return totalScore


def test():
    print(f"TEST")
    with open("./input/sample_inputs/day_2_sample.txt") as f:
        input = f.read()

    print(f"P1: {part1(input)}")
    assert part1(input) == 15
    print(f"P2: {part2(input)}")
    assert part2(input) == 12
    print("\n")


if __name__ == "__main__":
    with open("./input/day2.txt") as f:
        input = f.read()

    test()
    print("SOLUTION")
    print(f"P1: {part1(input)}")
    print(f"P2: {part2(input)}")
