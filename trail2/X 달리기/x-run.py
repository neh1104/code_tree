X = int(input())

# Please write your code here.

for i in range(X, 0, -1):
    len = 2*sum([t for t in range(1, i)])+i

    if len == X:
        print(2*i-1)
        break
    elif len < X:
        els = X-len
        cnt = 0
        for p in range(i, 0, -1):
            if p <= els:
                els -= p
                cnt += 1
        print(2*i-1+cnt)
        break