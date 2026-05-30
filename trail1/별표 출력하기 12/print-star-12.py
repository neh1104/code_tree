n = int(input())
print('* '*n)
for i in range(n-1):
    for j in range(n):
        if i>=j:
            print(' ', end = ' ')
            continue
        if j % 2 == 1:
            print('*', end = ' ')
            continue
        else:
            print(' ', end = ' ')
            continue
    print()

## 행렬의 특징을 살려 2차원 배열을 다루듯 접근
## 조건이 행과 열 별로 나누어지기 때문에 조금 더 이해하기 편한 감이 있음