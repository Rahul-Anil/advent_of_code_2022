x = list(
    map(eval, open("./input/sample_inputs/day_13_sample.txt").read().strip().split())
)

i2 = 1
i6 = 2


def f(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return f([x], y)
    else:
        if type(y) == int:
            return f(x, [y])

    for a, b in zip(x, y):
        v = f(a, b)
        if v:
            return v

    return len(x) - len(y)


for a in x:
    if f(a, [[2]]) < 0:
        i2 += 1
        i6 += 1
    elif f(a, [[6]]) < 0:
        i6 += 1

print(i2 * i6)
