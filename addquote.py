# Prints existing quotes
qfile = open('myfavquotes.txt', 'r')
quotes = qfile.readlines()
print(f"your existing quotes are as follows:\n {quotes}")

# Scans new quote
qfile = open('myfavquotes.txt', 'a')
newquote = input("Enter your new quote:\n")
qfile.write(f"\n{newquote}")

# Prints updated list
qfile = open('myfavquotes.txt', 'r')
latestquotes = qfile.readlines()
print(f"Your quotes are as follows:\n {latestquotes}" )
qfile.close()


# ChatGPTs weird code below
# # File name to store quotes
# filename = "favorite_quotes.txt"

# # Step 1: Read and display existing quotes
# try:
#     with open(filename, "r") as file:
#         quotes = file.readlines()
#         print("Your favorite quotes:")
#         for quote in quotes:
#             print(f"- {quote.strip()}")
# except FileNotFoundError:
#     print("No quotes found. Let's add some!")

# # Step 2: Get a new quote from the user
# new_quote = input("Enter a new quote to add: ")

# # Step 3: Append the new quote to the list
# quotes.append(new_quote + "\n")

# # Step 4: Write updated quotes back to the file
# with open(filename, "w") as file:
#     file.writelines(quotes)

# print("Quote added successfully!")
