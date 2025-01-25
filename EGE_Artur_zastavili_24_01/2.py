def  f(x, y, z, w):
    return not(((not x) or y) and (not w)) or not (z and not(y and w))


for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if(f(x, y, z, w) == 0):
                    print(x, y, z, w, f(x, y, z, w))

