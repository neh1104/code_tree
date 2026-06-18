n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x, y):
    return 0<=x<n and 0<=y<n
MAX = 0
for i in range(n*n):
    for j in range(i+3, n*n):
        x = i//n
        y = i%n
        x2 = j//n
        y2 = j%n
        #print(x, y, x2, y2)
        if in_range(x2, y2+2) and in_range(x, y+2):
            S = sum(arr[x][y:y+3]) + sum(arr[x2][y2:y2+3])
            MAX = max(MAX, S)
            #print(arr[x][y:y+3], arr[x2][y2:y2+3])
            
print(MAX)