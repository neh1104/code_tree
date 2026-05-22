arr = list(map(int, input().split()))

ls = []
for i in arr:
    if i == 0:
        break
    ls.append(i)

print(f"{sum(ls)} {round(sum(ls)/len(ls), 1)}")