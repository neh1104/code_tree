s, q = input().split()
q = int(q)
Q = [int(input()) for _ in range(q)]

# Please write your code here.

for i in range(q):
    if Q[i] == 1:
        s = s[1:]+s[0]
    elif Q[i] == 2:
        s = s[-1]+s[:-1]
    else:
        s = s[::-1]
    print(s)