import heapq
from collections import deque

# grid = [
#     list(x)
#     for x in open("./input/sample_inputs/day_12_sample.txt").read().strip().splitlines()
# ]

grid = [list(x) for x in open("./input/day12.txt").read().strip().splitlines()]

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"

q = deque()
q.append((0, er, ec))

visited = {(er, ec)}

while q:
    d, r, c = q.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if (nr, nc) in visited:
            continue
        if ord(grid[nr][nc]) - ord(grid[r][c]) < -1:
            continue
        if grid[nr][nc] == "a":
            print(d + 1)
            exit(0)
        visited.add((nr, nc))
        q.append((d + 1, nr, nc))


print("DONE")
