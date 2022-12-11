monkeys = []

for group in (
    open("./input/sample_inputs/day_11_sample.txt").read().strip().split("\n\n")
):
    line = group.splitlines()
    monkey = []
    monkey.append(list(map(int, line[1].split(": ")[1].split(","))))
    monkey.append(eval("lambda old:" + line[2].split("=")[1]))
    monkey.append(int(line[3].split(" ")[-1]))
    monkey.append((int(line[4].split(" ")[-1]), int(line[5].split(" ")[-1])))
    monkeys.append(monkey)

# print(monkeys)

mod = 1
for monkey in monkeys:
    mod *= monkey[2]

counts = [0] * len(monkeys)

for _ in range(10000):
    for num, monkey in enumerate(monkeys):
        for i in monkey[0]:
            i = monkey[1](i)
            # i //= 3
            i %= mod
            m1, m2 = monkey[3]
            if i % monkey[2] == 0:
                monkeys[m1][0].append(i)
            else:
                monkeys[m2][0].append(i)
        counts[num] += len(monkey[0])
        monkey[0] = []

print(counts)
counts = sorted(counts, reverse=True)
print(f"monkeyBusiness: {counts[0]*counts[1]}")
