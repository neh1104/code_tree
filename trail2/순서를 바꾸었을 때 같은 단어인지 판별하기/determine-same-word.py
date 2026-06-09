word1 = input()
word2 = input()

# Please write your code here.

word1 = sorted(word1)
word2 = sorted(word2)

ch = 0
if len(word1) == len(word2):
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            ch = 1
            break
else:
    ch = 1
print('Yes' if ch == 0 else 'No')
    