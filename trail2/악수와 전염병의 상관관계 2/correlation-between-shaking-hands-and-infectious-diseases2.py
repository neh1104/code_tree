N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

ls = [[0, K] for i in range(N)]#개발자 개인의 정보 관리 첫번째 원소는 감염여부, 두번째는 전염 가능여부 카운트

ls[P-1][0] = 1
handshakes.sort(key = lambda x: x[0]) #시간 순서로 정렬
#print(*handshakes, sep = '\n')
for i in range(T):
    x = handshakes[i][1]-1; y = handshakes[i][2]-1 
    x_ch, y_ch = 0, 0
    if ls[x][0] == 1 and ls[x][1] > 0:
        y_ch = 1
        ls[x][1] -= 1
    
    if ls[y][0] == 1 and ls[y][1] > 0:
        x_ch = 1
        ls[y][1] -= 1
    if x_ch == 1:
        ls[x][0] = 1
    if y_ch == 1:
        ls[y][0] = 1
        
#print(ls)
for i in ls:
    print(i[0], end = '')