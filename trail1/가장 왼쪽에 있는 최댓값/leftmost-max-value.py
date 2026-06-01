n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

m_id = n
while True: 
    id = 0
    for i in range(0, m_id):
        if a[i] > a[id]:
            id = i
    print(id+1, end = ' ')
    if id == 0:
        break
    m_id = id
