N = int(input())
seat = input()

# Please write your code here.

def min_len(st):
    MIN = 100
    for i in range(N):
        if st[i] == '1':
            cnt = 1
            for j in range(i+1, N):
                if st[j] == '1':
                    MIN = min(MIN, cnt)
                    break
                cnt += 1
    return MIN

MAX = 0
for i in range(N):
    if seat[i] == '1':
        continue
    for j in range(i+1, N):
        if seat[j] == '1':
            continue
        
        st = seat[:i]+'1'+seat[i+1:j]+'1'+seat[j+1:]
        MAX = max(MAX, min_len(st))

print(MAX)