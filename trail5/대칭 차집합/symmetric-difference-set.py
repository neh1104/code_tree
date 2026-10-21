n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

a = set(A); b = set(B)
ab = a-b; ba = b-a       

sum = ab|ba

print(len(sum))