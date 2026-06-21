N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
gifts.sort(key = lambda x: (x[0]+x[1], x[0]//2+x[1]))
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
#print(P)
#print(S)
sum = 0
cnt = 0
MAX = 0
for i in range(N):
    sum = P[i]//2 +S[i]
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        else:
            sum += P[j]+S[j]
            cnt += 1
        if sum > B:
            #print(sum, cnt-1, i+1)
            cnt-=1
            break
    MAX = max(MAX, cnt)
            

print(MAX)