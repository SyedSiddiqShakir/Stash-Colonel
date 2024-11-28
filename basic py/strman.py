qfile = open('myfavquotes.txt', 'r')
f = qfile.readlines()
print(f)

print("Replace the quote with a new text")
newquote = input()

qfile = open('myfavquotes.txt', 'w')
qfile.write(newquote)
qfile.close()

print(f"Your new Quote is:\n{newquote}")

# with open('myfavquotes.txt', 'r') as qfile: