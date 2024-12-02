#mysentence = input("Enter your sentence: ")

myfile = open('mylom1.txt', 'r')
mylines = str(myfile.readlines())

# to_replace = [",", "!", "'", "\n", "-"]

# for char in to_replace:
#     mylines = mylines.replace(char, " ")

words = mylines.lower().replace(".", " ").split()
unique_words = sorted(set(words))

print(f"Sorted Uniques words: {unique_words}")
print(f"Total Number of words: {len(words)}")
print(f"Number of unique words: {len(unique_words)}")