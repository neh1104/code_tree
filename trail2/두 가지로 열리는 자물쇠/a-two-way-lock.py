N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
cnt = 0
# Please write your code here.
def rmswjq(i, j, k, n1, n2, n3):
    return min(abs(i-n1), N-(abs(i-n1))) <= 2 and min(abs(j-n2), N-(abs(j-n2))) <= 2 and min(abs(k-n3), N-(abs(k-n3))) <= 2
for i in range(N):
    for j in range(N):
        for k in range(N):
            if rmswjq(i, j, k, a1, b1, c1) or rmswjq(i, j, k, a2, b2, c2):
                cnt += 1

print(cnt) 