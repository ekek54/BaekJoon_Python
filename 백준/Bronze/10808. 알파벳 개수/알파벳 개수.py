import sys

alpha_dict = {chr(97 + i):0 for i in range(26)}
word = sys.stdin.readline().rstrip()
for i in range(len(word)):
    alpha_dict[word[i]] += 1
print(*alpha_dict.values())