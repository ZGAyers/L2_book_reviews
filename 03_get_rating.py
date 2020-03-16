# Component 03 - Get the users genral rating and checks it

import math

# Get Rating Function goes here
def get_rating():

    error = "Please enter a number between 1 - 5"
    rating_reason = []

    valid = False
    while not valid:
        try:
            response = float(input("Rating: "))

            if response > 5:
                print("Ok - the rating will be recorded as '5' - the highest possible rating")
                response = 5
                reason = input("Please give a reason for rating this book so highly: ")

            elif response < 1:
                print("Ok - the rating will be recorded as '1' - the lowest possible rating")
                response = 1
                reason = input("Please enter a reason for the low rating: ")

            elif response % 1 != 0:
                valid_round = False
                while not valid_round:
                    round_it = input("You have entered a decimal, would you like us to round up or down: ").lower()

                    if round_it == "up":
                        default_reason = "The book was worth more than {} stars.".format(int(response))
                        response = math.ceil(response)
                        break

                    elif round_it == "down":
                        default_reason = "It is not worth {} stars.".format(math.ceil(response))
                        response = int(response)
                        break
                    else:
                        print("Please enter <up> or <down>")

                reason = input("Please enter a reason for rounding the rating {}: ".format(round_it))
                if reason == "":
                    print("You left the reason blank, so we have put in a reason for you.")
                    reason = default_reason
            else:
                response = int(response)
                reason = input("Please explain why you gave a rating of {}: ".format(response))

            rating_reason.append(response)
            rating_reason.append(reason)
            return rating_reason

        except ValueError:
            print(error)


# ---main routine---
rate_reason = get_rating()
print()
book_rating = rate_reason[0]
book_reason = rate_reason[1]

print("Rating: {}".format(book_rating))
print("Reason: {}".format(book_reason))
