def f(s):
    while '4444' in s or '844' in s or '84' in s:
        if '4444' in s:
            s = s.replace('4444', '884', 1)
        if '844' in s:
            s = s.replace('844', '488', 1)
        if '84' in s:
            s = s.replace('84', '3343', 1)
    return s
ch = 0
for i in range(4, 10000):
    s = '8' + '4' * i
    print(i, ' ', ch + 1)
    if len(f(s)) <= 20:
        ch = i
print(' ', ch + 1)

