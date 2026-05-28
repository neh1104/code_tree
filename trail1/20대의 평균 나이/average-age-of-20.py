cnt = 0
sum = 0
while True:
    c = int(input())
    if 20 <= c <= 29:
        sum += c
        cnt += 1
        continue
    print(f"{sum/cnt:.2f}") #round()함수는 소수점 뒤 의미없는 0은 제거함! 
    break                   #따라서 정해진 자리까지 출력하고자 한다면 포맷팅이 정답!
    