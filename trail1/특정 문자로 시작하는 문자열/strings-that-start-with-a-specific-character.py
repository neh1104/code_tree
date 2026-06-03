n = int(input())

a = [input() for _ in range(n)]

k = input()

ln = 0
cnt = 0
for ele in a:
    if ele[0] == k:
        ln += len(ele)
        cnt += 1
print(f"{cnt} {ln/cnt:.2f}")