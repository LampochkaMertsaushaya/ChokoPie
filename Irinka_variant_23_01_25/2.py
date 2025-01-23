def f(x, y, z, w):
    return (z != x) <= ((w <= (not y)) and (y <= x))

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                print(x, y, z, w, f(x, y, z, w))