# Complete v1 of book review program

import random
import math

# Functions go here


# Not Blank function goes here
def not_blank(question, error_msg,):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if __name__ == '__main__':
            if response == "":
                print(error)
                continue

            elif has_errors != "":
                print(error)
                continue

            else:
                return response


# Get rating function
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
                    round_it = input(
                        "You have entered a decimal, would you like us to round up or down: ").lower()

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


# Offers users list of options, can be set to choose random response
def text_helper(question, possible_answers, items_per_line, required=None):
    error = "This is a required field. Please choose an item from the list" \
                    "or type in a word / phrase"
    print(question)

    valid = False
    while not valid:

        # Output numbered list with specified number of items per line
        count_ans = 0

        for item in possible_answers:
            print("{}. {}".format(possible_answers.index(item) + 1, item),
                    end="\t")
            count_ans += 1
            if count_ans % items_per_line == 0:
                print()

        print()
        print()
        response = input("Choose: ")

        # Checks that response has been given if required
        if required == "yes" and response == "":
            print(error)
            continue

        # check if the response is a number / choice, if it is, change
        # it to the option in the list

        try:
            response = int(response) - 1
            # Check that number is an option
            if 0 <= int(response) < len(possible_answers):
                # response is a choice in the list, return word
                # that matches chosen number
                response = possible_answers[response]
                return response
            else:
                print(error)

        except ValueError:
            # User has typed in text, return it to the main routine
            return response


# Make a list function
def make_list(file_name):
    file_name = file_name + ".txt"  # add .txt to names to make it easier to call
    list_name = open(file_name).read().splitlines()
    return list_name


# Main routine goes here..

# Set up blank Adjective Lists
genre_list = []
all_negative = all_positive = all_neutral = []
action_list = fantasy_list = funny_list = historical_list = scary_list = []

# **Set up genre list and sort it**
genre_list = make_list("genre")
all_negative = make_list("all_negative")
all_positive = make_list("all_positive")
all_neutral = make_list("all_neutral")

action_list = make_list("action")
fantasy_list = make_list("fantasy")
funny_list = make_list("funny")
historical_list = make_list("historical")
scary_list = make_list("scary")


# ask the user for the title of the book
title = not_blank("Title: ",
                  "Please type in a title")

# ask user for the author and if no author is given set to "Anonymous"
author = input("Author: ")

if author == "":
    print("Since you left this field blank the author name will become 'Anonymous'.")
    author = "Anonymous"

rate_reason = get_rating()
print()
book_rating = rate_reason[0]
book_reason = rate_reason[1]

# genre of book
genre_list = [x.lower() for x in genre_list]

genre = text_helper("Please choose a genre", genre_list, 4, "yes")








