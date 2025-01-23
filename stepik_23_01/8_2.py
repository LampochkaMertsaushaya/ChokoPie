
choko_0 = 0
choko = 0
for a1 in range(0, 8):
    for a2 in range(0, 8):
        for a3 in range(0, 8):
            for a4 in range(0, 8):
                for a5 in range(0, 8):
                    arr = [a1, a2, a3, a4, a5]
                    for i in range(1, 4):
                        if (arr[i-1] % 2 == 0 and arr[i+1] % 2 != 0) or (arr[i-1] % 2 != 0 and arr[i+1] % 2 == 0):
                            choko_0 +=1
                    if choko_0 == 3:
                        choko += 1
                    choko_0 = 0


print(choko)