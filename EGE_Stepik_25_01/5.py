def f(n):
    num = bin(n)
    if n % 2 == 0:
        s = str(num).replace('1', '11')
        num = int(s, 2)
    else:
        s = str(num).replace('0', '00')
        num = int(s[1::], 2)
    return num

for i in range(2, 100):
    if f(i) > 70:
        print(i)
        break
