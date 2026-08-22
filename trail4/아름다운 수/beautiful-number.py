n = int(input())

# Please write your code here.

def beautiful(d):
    global cnt
    if d == n:
        cnt += 1
        return 
    elif d > n:
        return
    
    for i in range(1, 5):
        beautiful(d + i)

cnt = 0
beautiful(0)
print(cnt)