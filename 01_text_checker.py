# Component 1 - Text Checker / Not Blank function


# Not Blank function goes here
def not_blank(question, error_msg,):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if response == "":
            print(error)
            continue

        elif has_errors != "":
            print(error)
            continue

        else:
            return response

title = not_blank("Title: ",
                  "Please type in a title")

print("You are reviewing {}".format(title))
