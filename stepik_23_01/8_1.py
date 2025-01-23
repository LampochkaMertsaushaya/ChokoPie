spisok = ['К', 'А', 'Л', 'И', 'Й']

choko = 0
for a1 in spisok:
    for a2 in spisok:
        for a3 in spisok:
            for a4 in spisok:
                for a5 in spisok:
                    for a6 in spisok:
                        s = a1 + a2 + a3 + a4 + a5 + a6
                        if s.count('Й') <= 1 and a1 != 'Й' and a6 != 'Й' and 'ЙИ' not in s and 'ИЙ' not in s:
                            choko += 1

print(choko)

