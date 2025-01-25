def f(x, y, z, w):
    return (x <= y) and (z == (w <= x)) and (not w)

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if f(x, y, z, w) == 1:
                    print(x, y, z, w, f(x, y, z, w))