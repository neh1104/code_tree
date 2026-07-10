N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

odd = 0
even = 0

for i in range(N):
    if numbers[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    print(odd*2 +1)
elif even == odd:
    print(2*even)
else:
    if (odd - even)%3 == 2:
        el = 1 
    elif (odd-even)%3 == 1:
        el = -1
    else:
        el = 0
    print(2*even + 2*((odd-even)//3)+el) 