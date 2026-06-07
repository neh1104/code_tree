n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def f(n):
    if n == 1:
        return arr[0]
    return max(f(n-1), arr[n-1]) 

print(f(n))