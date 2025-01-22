s = open('24.txt').readline()
strok = ''
arr = []
for i in s:
    if i not in strok:
        strok += i
    else:
        arr.append(len(strok))
        strok = i
arr.append(len(strok))
print(max(arr))
