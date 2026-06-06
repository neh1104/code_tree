n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def bubun(x, y):
    for i in range(n1 - n2 + 1):
        for j in range(n2):
            if x[i+j] != y[j]:
                break
            if j == n2 - 1:
                return True
    return False

print('Yes' if bubun(a, b) else 'No')
             