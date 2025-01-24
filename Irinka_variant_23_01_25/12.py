def f(s):
    while '00' not in s:
        s = s.replace('011', '20', 1)
        s = s.replace('022', '10', 1)
        s = s.replace('01', '220', 1)
        s = s.replace('02', '110', 1)
    return s

choko_max = 0
for i in range(1, 1000):
    s = '0' + '1' * i + '2'* i + '0'
    s1 = f(s)
    if (s1.count('2') < 70) and (s1.count('1') == 47):
        print(s1.count('2') - 1)


for i in range(1, 100):
    s = '0' + i * '1' + i * '2' + '0'
    while '00' not in s:
        s = s.replace('011', '20', 1)
        s = s.replace('022', '10', 1)
        s = s.replace('01', '220', 1)
        s = s.replace('02', '110', 1)
    if s.count('1') == 47 and s.count('2') < 70:
        print(i)
