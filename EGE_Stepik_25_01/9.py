s = [list(map(int, x.split(';'))) for x in open('9.txt')]

k = 0
ans = []
for line in s:
    if len(set(line)) == len(line):
        if max(line) < sum(line) - max(line):
            k += 1
print(k)