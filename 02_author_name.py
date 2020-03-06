# Component 2 - Author Name

author = []
author_input = input("Author: ")

if author_input == "":
    print("Since you left this field blank the author name will become 'Anonymous'.")
    author = "Anonymous"
else:
    author.append(author_input)

print("The authors name is")
