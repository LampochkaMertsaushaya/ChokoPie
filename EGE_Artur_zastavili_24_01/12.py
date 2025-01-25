def f(s):
    while '12' in s or '322' in s or '222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    return s

for i in range (4, 10000):
    s = '1' + '2' * i
    s1 = f(s)
    ch = 0
    for j in s1:
        ch += int(j)
    if ch == 15:
        print(i)
        break