N = int(input())
seats = input()

# Please write your code here.
mid = []
if seats[0] != '1':
    mid.append(0)
if seats[-1] != '1':
    mid.append(N-1)
ch = 0
las = 0
for i in range(N):
    if seats[i] == '1':
        if ch:
            mid.append(i-(i-last)//2)
        last = i
        ch = 1
        
def MAX(ls):
    m = 1000
    cnt = 1000
    for i in ls:
        if i == '1':
            m = min(m, cnt)
            cnt = 1
        else:
            cnt += 1
    return m

Max = 0
for i in mid:
    i = int(i)
    ls = seats[:i]+'1'+seats[i+1:]
    #print(ls)
    m = MAX(ls)
    Max = max(m, Max)

print(Max)