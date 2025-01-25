def f(s):
    if s.count('0') == 1:
        if s.find('0') == 0:
            if int(s[1]) % 2 == 0:
                return 1
            else:
                return 0
        elif  s.find('0') == 5:
            if int(s[4]) % 2 == 0:
                return 1
            else:
                return 0
        else:
            if int(s[s.find('0') - 1]) % 2 == 0 and int(s[s.find('0') + 1]) % 2 == 0:
                return 1
            else:
                return 0



alf = '012345'
ch = 0

print(alf[1::])
for a1 in alf[1::]:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    for a6 in alf:
                        s = a1 + a2 + a3 + a4 + a5 + a6
                        if f(s) == 1:
                            ch += 1
print(ch)