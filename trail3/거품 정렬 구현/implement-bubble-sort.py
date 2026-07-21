n = int(input())
a = list(map(int, input().split()))

while True:
    srt = 1
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
            srt = 0
    if srt:
        break

print(*a)