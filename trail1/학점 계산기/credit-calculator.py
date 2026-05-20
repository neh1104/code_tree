n = int(input())

ls = list(map(float, input().split()))

sls = sum(ls) / n
print(f"{sls:.1f}")

if sls >= 4.0:
    print("Perfect")
elif sls >= 3.0:
    print("Good")
else:
    print("Poor")