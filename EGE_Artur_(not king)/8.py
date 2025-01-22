spisok = ['K', 'Z', 'B', 'C']
ch = 0
for a1 in spisok:
    for a2 in spisok:
        for a3 in spisok:
            for a4 in spisok:
                for a5 in spisok:
                    s = a1 + a2 + a3 + a4 + a5
                    if s.count('Z') <= 2 and not('KB' in s) and not('BK' in s):
                        ch += 1

print(ch)