f = {}
p = {}

for line in open(0).read().strip().splitlines():
    a, b = line.split(";")
    f[a[6:8]] = int(a.split("=")[1])
    p[a[6:8]] = "".join(b.strip().split(" ")[4:]).split(",")
    # print("".join(b.strip().split(" ")[4:]).split(","))

t = 0
