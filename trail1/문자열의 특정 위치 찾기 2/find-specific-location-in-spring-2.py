a = ["apple", "banana", "grape", "blueberry", "orange"]
n = input()

cnt = 0
ch = False
for i in a:
    ch = False
    for j in range(len(i)):
        if i[j] == n and j in [2, 3]:
            ch = True
            cnt += 1
    if ch == True:
        print(i)
            

print(cnt)