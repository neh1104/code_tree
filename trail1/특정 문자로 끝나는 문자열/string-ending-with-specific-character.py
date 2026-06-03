a = [input() for _ in range(10)]
key = input()

cnt = 0
for ele in a:
    if ele[-1] == key:
        print(ele)
        cnt += 1

print('None' if cnt == 0 else '')