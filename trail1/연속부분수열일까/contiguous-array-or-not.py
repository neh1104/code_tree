n_1, n_2 = map(int, input().split())

a_ls = list(map(int, input().split()))
b_ls = list(map(int, input().split()))

bubun = False

for i in range(n_1):
    if bubun == True:
        break
    if len(a_ls[i:-1]) + 1 < n_2:
        #print('Over')
        break
    cnt = 0
    if a_ls[i] == b_ls[0]:
        for j in range(n_2):
            if a_ls[i+j] == b_ls[j]:
                cnt += 1
                if cnt == n_2:
                    bubun = True
            else:
                break

        

print('Yes' if bubun == True else 'No')