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

for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue

    dists[valve] = {}
    visited = {valve}

    q = deque([(0, valve)])

    while q:
        dis, pos = q.popleft()
        for neigh in tunnels[pos]:
            if neigh in visited:
                continue
            visited.add(neigh)

            if valves[neigh]:
                dists[valve][neigh] = dis + 1

            q.append((dis + 1, neigh))


print(dists)
