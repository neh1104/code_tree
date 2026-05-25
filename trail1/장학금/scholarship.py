m, h = map(int, input().split())

if m >= 90:
    if h >= 95:
        print(100000)
    elif h >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)