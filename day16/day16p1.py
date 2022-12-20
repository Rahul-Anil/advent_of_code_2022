from collections import deque

valves = {}
tunnels = {}

for line in open(0).read().strip().splitlines():
    valve = line.split()[1]
    flow = int(line.split(";")[0].split("=")[1])
    targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
    valves[valve] = flow
    tunnels[valve] = targets

dists = {}
nonempty = []

for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue

    if valve != "AA":
        nonempty.append(valve)

    dists[valve] = {valve: 0}
    visited = {valve}

    q = deque([(0, valve)])  # first in first out

    while q:
        d, p = q.popleft()
        for neigh in tunnels[p]:
            if neigh in visited:
                continue

            visited.add(neigh)
            if valves[neigh]:
                dists[valve][neigh] = d + 1
            q.append((d + 1, neigh))

    del dists[valve][valve]

indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

cache = {}


def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]

    maxval = 0
    for neigh in dists[valve]:
        bit = 1 << indices[neigh]  # puts 0 on the right side
        if bitmask & bit:  # if all valves are open then this is going to be 0
            continue
        remtime = time - dists[valve][neigh] - 1

        if remtime <= 0:
            continue

        maxval = max(
            maxval,
            dfs(remtime, neigh, bitmask | bit)
            + valves[neigh]
            * remtime,  # the bitwise operation over there is used to turn on that bit
        )

    cache[(time, valve, bitmask)] = maxval

    return maxval


print(dfs(30, "AA", 0))
