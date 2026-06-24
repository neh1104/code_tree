n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.

#print(h)
def iceburg(a):
    cnt = 1 if a[0] > 0 else 0
    for i in range(1, n):
        if a[i-1]*a[i] < 0 and a[i] > 0:
            cnt += 1
    return cnt
        
    

MAX = 0
for i in range(max(h)):
    ice = []
    for j in h:
        ice.append(j-i if j-i >= 1 else -1)
    
    #print(ice)
    MAX = max(MAX, iceburg(ice))

print(MAX)