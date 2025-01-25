s = open('24.txt').readline()

while 'FSRQ' in s:
    s = s.replace('FSRQ', '*')

ch = 0
ch_1 = 0
arr = []
arr1 = []
for i in s:
    if i == '*':
        ch += 1
    elif i != 'W' and i != 'G':
        ch_1 += 1
    else:
        arr.append(ch)
        arr1.append(ch_1)
        ch, ch_1 = 0, 0

ch = 0
for i in range(0, len(arr) - 1):
    if (arr[i] == 80) and (arr1[i] > ch):
        ch = arr1[i]

print(80 * 4 + ch)