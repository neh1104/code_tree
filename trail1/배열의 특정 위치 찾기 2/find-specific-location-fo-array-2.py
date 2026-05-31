arr = list(map(int, input().split()))

odd = sum(arr[::2])
even = sum(arr[1::2])

print(abs(odd-even))