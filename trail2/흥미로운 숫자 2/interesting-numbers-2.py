X, Y = map(int, input().split())

# Please write your code here.
CNT = 0
for i in range(X, Y+1):
    i = str(i)
    for k in range(10):
        if i.count(str(k)) == len(i)-1:
            CNT += 1
print(CNT)        