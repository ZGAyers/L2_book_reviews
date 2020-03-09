# Component 2 - Author Name

author = input("Author: ")

if author == "":
    print("Since you left this field blank the author name will become 'Anonymous'.")
    author = "Anonymous"


print("The authors name is {}".format(author))
