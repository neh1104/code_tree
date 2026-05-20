ls = list(map(int, input().split()))

ls_2 = []
for ele in ls:
    if ele >= 250:
        break
    ls_2.append(ele)

sum_ls = sum(ls_2)
print(sum_ls, f"{sum_ls / len(ls_2):.1f}")