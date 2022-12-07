class dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = {}
        self.children = {}
        self.size = 0

    def mkdir(self, name):
        return self.children.setdefault(name, dir(name, parent=self))

    def touch(self, size, name):
        self.files[name] = int(size)

    def getSize(self) -> int:
        self.size = sum(self.files.values())
        for c in self.children.values():
            self.size += c.getSize()
        return self.size

    @property
    def root(self):
        return self if self.parent is None else self.parent.root


def part1(input: str):
    stack = []
    input = input.splitlines()
    cwd = dir(name="/", parent=None)
    stack.append(cwd)
    for line in input[1:]:
        if line[0] == "$":
            if line[2] == "c":
                D = line[5:]
                if D == "..":
                    cwd = cwd.parent
                else:
                    cwd = cwd.mkdir(D)
                    if cwd not in stack:
                        stack.append(cwd)
        else:
            x, y = line.split()
            if x == "dir":
                continue
            else:
                cwd.touch(x, y)

    dirSize = {}
    sum = 0
    for s in stack:
        dirSize[s.name] = s.getSize()
        if s.getSize() <= 100000:
            

    print(dirSize)


if __name__ == "__main__":
    input = open("./input/sample_inputs/day_7_sample.txt").read().strip()
    part1(input)
