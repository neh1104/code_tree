text = input()
pattern = input()

# Please write your code here.

def id():
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            if j == len(pattern) - 1:
                return i
    return -1

print(id())