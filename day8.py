import copy


def up(row, col, val, tree):
    print("UP")
    count = 1
    row -= 1
    while row != -1:
        if tree[row][col] > val or tree[row][col] == val:
            print(f"count: {count}")
            return count
        row -= 1
        count += 1
    print(f"count: {count}")
    return count - 1


def down(row, col, val, tree):
    print("DOWN")
    count = 1
    row += 1
    while row != len(tree):
        if tree[row][col] > val or tree[row][col] == val:
            print(f"count: {count}")
            return count
        row += 1
        count += 1
    print(f"count: {count}")
    return count - 1


def left(row, col, val, tree):
    print("LEFT")
    count = 1
    col -= 1
    while col != -1:
        if tree[row][col] > val or tree[row][col] == val:
            print(f"count: {count}")
            return count
        col -= 1
        count += 1
    print(f"count: {count}")
    return count - 1


def right(row, col, val, tree):
    print("RIGHT")
    count = 1
    col += 1
    while col != len(tree[0]):
        if tree[row][col] > val or tree[row][col] == val:
            print(f"count: {count}")
            return count
        col += 1
        count += 1
    print(f"count: {count}")
    return count - 1


def solve(input: str):
    input = input.strip().splitlines()
    tree = [[int(t) for t in line] for line in input]
    rowLen = len(tree)
    colLen = len(tree[0])
    edgePoints = rowLen * 2 + colLen * 2 - 4  # all edge points are visible

    counter = []

    # for row in range(1, rowLen - 1):
    #     for col in range(1, colLen - 1):
    #         if (
    #             up(row, col, tree[row][col], tree)
    #             or down(row, col, tree[row][col], tree)
    #             or left(row, col, tree[row][col], tree)
    #             or right(row, col, tree[row][col], tree)
    #         ):
    #             counter += 1

    for row in range(1, rowLen - 1):
        for col in range(1, colLen - 1):
            print(f"tree: {tree[row][col]}")
            temp = (
                up(row, col, tree[row][col], tree)
                * down(row, col, tree[row][col], tree)
                * left(row, col, tree[row][col], tree)
                * right(row, col, tree[row][col], tree)
            )
            counter.append(temp)

    # print(f"counter: {counter}")
    # print(f"total: {counter + edgePoints}")
    print(f"max:  {max(counter)}")


# def solve(input: str):
#     tree = {}
#     for row, line in enumerate(input.strip().splitlines()):
#         for col, height in enumerate(line):
#             tree[row, col] = int(height)


if __name__ == "__main__":
    input = open("./input/sample_inputs/day_8_sample.txt").read().strip()
    inputMain = open("./input/day8.txt").read().strip()
    solve(input)
    solve(inputMain)
