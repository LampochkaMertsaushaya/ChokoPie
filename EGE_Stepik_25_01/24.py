s = open('24.txt').readline()
spisok = ['0', '1', '2', '3', '4']
spisok_2 = ['-', '+']
ch = 0
op = 0
arr = []
for i in range(0, len(s)):
    if op == 1:
        if s[i] in spisok and s[i] != 0:



    elif s[i] in spisok:
        ch += 1
    else:
        op += 1



