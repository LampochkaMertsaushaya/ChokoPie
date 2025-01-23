spisok = ['А','К','Р','У']

ch = 0
for a1 in spisok:
    for a2 in spisok:
        for a3 in spisok:
            for a4 in spisok:
                for a5 in spisok:
                    ch += 1
                    s = a1 + a2 + a3 + a4 + a5
                    if (s == 'УКАРА'):
                        print(ch)