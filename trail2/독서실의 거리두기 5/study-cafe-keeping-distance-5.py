N = int(input())
seat = input()

# Please write your code here.
def close(i):
    right, left = 20, 20
    for j in range(i+1, N):
        if seat[j] == '1':
            right = j-i
            break
    for j in range(i-1, -1, -1):
        if seat[j] == '1':
            left = i-j
            break
    #print(i, right, left)
    return (min(right, left), i)

MAX = (0, 0)
for i in range(N):
    if seat[i] == '0':
        #print(i)
        dist = close(i)
        #print(dist)
        if MAX[0] < dist[0]:
            MAX = dist
 #           print(MAX)

seat = seat[:MAX[1]]+'1'+seat[MAX[1]+1:]

#print(seat)
MAX = 20
for i in range(N):
    if seat[i] == '1':
        dist = close(i)
    
        MAX = min(MAX, dist[0]) 

print(MAX)