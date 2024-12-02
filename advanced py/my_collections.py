# from collections import Counter
'''
a = Counter('siddiq')
print(a)
b = Counter({'me': 25, 'you': 23, 'him': 22})
print(b)
c = Counter(sir = 44, mam = 51, her = 76)
print(c)
'''

newfile = open('mevsmustaeenchess.txt', 'r')
newtext = str(newfile.readlines())
words = newtext.split(".")

new_words = []



print(f"new words are {new_words}")
print(type(new_words[1]))



# for char in words:
#     if isinstance(char, str):
#         new_words.append(char)



#print("break")
#print(newtext)
# new_words = []
# for char in words:
#     if isinstance(char, str):
#         new_words.append(char)
# print(new_words)



# newlist = Counter(newlist)
# print(newlist.most_common(3))