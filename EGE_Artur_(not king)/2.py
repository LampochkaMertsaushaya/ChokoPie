def f(x, y, z, w):
    return not((((((w and x)== x)or 1)<= z)or (not x))and y)


for x in (0, 1):
    for y in (0, 1):
        for w in (0, 1):
            for z in (0, 1):
                if f(x, y, z, w) == 0:
                    print(y, x, z, w, '|', f(x, y, z, w))
