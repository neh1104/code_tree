N, L = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.

a.sort(reverse = True)

def count_h(A, i):
    cnt = -1
    for a in A:
        cnt += 1
        if a < i and cnt < i:
            return 0
    return 1

st = N if N <= max(a)+1 else max(a)+1
for i in range(st, -1, -1):
    cnt = 0
    A = a[::]
    for j in range(N):
        if cnt == L:
            #print(i, 'b')
            break
        if A[j] < i:
            A[j] += 1
            cnt += 1
    if count_h(A, i):
        #print(A)
        print(i)
        break
        