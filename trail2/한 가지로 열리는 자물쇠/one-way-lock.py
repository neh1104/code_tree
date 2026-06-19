N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
cnt = 0
for i in range(1, N+1):
    for j in range(1,N+1):
        for k in range(1, N+1):
            A = abs(i-a); B = abs(j-b); C = abs(k-c)
            if A <= 2 or B <= 2 or C <= 2:
                cnt += 1

print(cnt)