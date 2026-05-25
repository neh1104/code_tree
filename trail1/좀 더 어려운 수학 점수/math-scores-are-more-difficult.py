a_m, a_e = map(int, input().split())
b_m, b_e = map(int, input().split())

if a_m > b_m or b_m > a_m:
    print('A' if a_m > b_m else 'B')
else:
    print('A' if a_e > b_e else 'B')