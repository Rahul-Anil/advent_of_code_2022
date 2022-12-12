from collections import deque

# grid = [
#     list(x)
#     for x in open("./input/sample_inputs/day_12_sample.txt").read().strip().splitlines()
# ]

grid = [list(x) for x in open("./input/day12.txt").read().strip().splitlines()]

for r, row in enumerate(grid):
    for c, items in enumerate(row):
        if grid[r][c] == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if grid[r][c] == "E":
            er = r
            ec = c
            grid[r][c] = "z"

q = deque()
q.append((0, sr, sc))

visited = {(sr, sc)}

while q:
    d, r, c = q.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if (nr, nc) in visited:
            continue
        if ord(grid[nr][nc]) - ord(grid[r][c]) > 1:
            continue
        if nr == er and nc == ec:
            print(d + 1)
            exit(0)

        visited.add((nr, nc))
        q.append((d + 1, nr, nc))
