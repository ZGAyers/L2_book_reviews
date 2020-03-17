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
overall = []
underlying_story = []
action_list = fantasy_list = funny_list = historical_list = scary_list = []
writing_negative = writing_positive = writing_neutral = []
ending = []
book_is = []

# **Set up genre list and sort it**
genre_list = make_list("genre")
all_negative = make_list("all_negative")
all_positive = make_list("all_positive")
all_neutral = make_list("all_neutral")

overall = make_list("overall")
book_is = make_list("book_is")

writing_negative = make_list("writing_negative")
writing_neutral = make_list("writing_neutral")
writing_positive = make_list("writing_positive")

underlying_story = make_list("underlying_story")
ending = make_list("ending")

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


# choose adjectives and sentences from rating
if book_rating > 2:
    feeling = "enjoyed"
    feeling2 = "like a breath of fresh air"
    recommend = "recommend"
else:
    feeling = "disliked"
    feeling2 = "disappointing as the book has potential"
    recommend = "not recommend"
# genre of book
genre_list = [x.lower() for x in genre_list]

genre = text_helper("Please choose a genre", genre_list, 4, "yes")

# setting of the book
setting = input("Please enter the setting/place the story is set in: ")

# main character name
character = input("Please enter the main characters name: ")

# plot of the book
plot = input("Please enter a plot summary: They are ")

# overall thoughts on book
overall = [x.lower() for x in overall]

overall_choice = text_helper("Please choose what you thought of the book overall",
                                 overall, 4, "yes")
# Ending of the book
ending = [x.lower() for x in ending]

ending_choice = text_helper("What did you think of the ending?",
                                 ending, 4, "yes")


# If the reader liked the book...
if book_rating > 3:
    # about the authors writing - positive
    writing_positive = [x.lower() for x in writing_positive]
    writing_choice = text_helper("Please choose what you thought of the authors writing",
                                 writing_positive, 4, "yes")

    all_positive = [x.lower() for x in all_positive]

    # first adjective - positive
    first_adjective = text_helper("Please choose an adjective describing the book",
                                  all_positive, 4, "yes")
    # second adjective - positive
    second_adjective = text_helper("Please choose another adjective describing the book",
                                  all_positive, 4, "yes")
    # third adjective - positive
    third_adjective = text_helper("Please choose another adjective describing the book",
                                  all_positive, 4, "yes")

# If the the reader didn't like the book...
elif book_rating < 3:
    # about the authors writing - negative
    writing_negative = [x.lower() for x in writing_negative]
    writing_choice = text_helper("Please choose what you thought of the authors writing",
                                 writing_negative, 4, "yes")

    # first adjective - negative
    all_negative = [x.lower() for x in all_negative]
    first_adjective = text_helper("Please choose an adjective describing the book",
                                  all_negative, 4, "yes")
    # second adjective - negative
    second_adjective = text_helper("Please choose another adjective describing the book",
                                  all_negative, 4, "yes")
    # third adjective - negative
    third_adjective = text_helper("Please choose another adjective describing the book",
                                  all_negative, 4, "yes")

# If the reader didn't mind the book...
else:
    # about the authors writing - neutral
    writing_neutral = [x.lower() for x in writing_neutral]
    writing_choice = text_helper("Please choose what you thought of the authors writing",
                                 writing_neutral, 4, "yes")

    # first adjective - neutral
    all_neutral = [x.lower() for x in all_neutral]
    first_adjective = text_helper("Please choose an adjective describing the book",
                                  all_neutral, 4, "yes")
    # second adjective - neutral
    second_adjective = text_helper("Please choose another adjective describing the book",
                                  all_neutral, 4, "yes")
    # third adjective - neutral
    third_adjective = text_helper("Please choose another adjective describing the book",
                                  all_neutral, 4, "yes")

# reader gives adjective to say what the book is...
book_is = [x.lower() for x in book_is]
book_is_choice = text_helper("The book is...", book_is, 4, "yes")

# underlying story
underlying_story = [x.lower() for x in underlying_story]
underlying_story_choice = text_helper("What did you think of the underlying story: ", underlying_story, 4, "yes")

# First Sentence
first = "{} and {} are two words I would use to describe the book by {}.".format(first_adjective.title(), second_adjective,
                                                                                 author)

# Second Sentence
if plot != "" and setting != "" and character != "":
    second = "Set in {}, we follow {} who is {}.".format(setting, character.title(), plot)
elif plot != "" and character != "":
    second = "In '{}' we follow {} who is {}.".format(title.title(), character.title(), plot)
elif plot != "":
    second = "In '{}' we are thrown into the story as our character {}.".format(title.title(), plot)
else:
    second = "'{}' is an {} {} book that I immensely {} reading".format(title.title(), third_adjective, genre, feeling)

# Third Sentence
third = "The writing style in this book is {} which is {}.".format(writing_choice, feeling2)

# Fourth Sentence
fourth = "The underlying story is {} and the ending is {}".format(underlying_story_choice, ending_choice)

# Put together the review
review = first, second, third, fourth

for item in review:
    print(item)
