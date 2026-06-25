A, B, C = map(int, input().split())

# Please write your code here.
sum = []

for a in range(1000):
    if A*a >= C:
        break
    for b in range(1000):
        if B*b > C:
            break
        
        if A*a + B*b <= C:
            sum.append(A*a+B*b)

print(max(sum))