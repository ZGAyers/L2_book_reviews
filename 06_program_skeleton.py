# Component 06 - Review Skeleton

import random

# -- Functions --

# Main routine goes here

# lists /  dictionaries
vowels = ["a", "e", "i", "o", "u"]
# Get inputs

title = "Chain of Gold"
author = "Cassandra Clare"

rating = 4.5
up_down = "up"
reason = "as the book is worth more than 4 stars"
genre = "fantasy"

plot = "James and Cordelia try and save London"
# plot = ""
# setting = "1900 London"
setting = ""

feeling = "delight"
first_adjectives = ["exciting", "fast-pasted"]
second_adjectives = "addictive"
writing_style = "unique"
extra = ["appeasing", "brilliant", "beautiful"]
overall = "liked"
recommend = "yes"

# first sentence
if plot != "" and setting != "":
    first = "Set in {}, '{}' is {}.".format(setting, title, plot)
elif plot != "":
    # make first letter capital
    first = "{}, {} is what I would call {} in {}.".format(first_adjectives[0].title(), first_adjectives[1], plot,  title)
else:
    first = "{} is both {} and {}.".format(title.title(), first_adjectives[0], first_adjectives[1])

# *** Second Sentence ***
choose_second = random.randint(1, 2)  # choose '1' or '2' randomly

# if first letter of the adjective is a vowel, use 'an' otherwise use 'a'
if second_adjectives[0] in vowels:
    determiner = "an"
else:
    determiner = "a"

if choose_second == 1:
    second = "{} has created {} {} {}.".format(author, determiner, second_adjectives, feeling)
else:
    second = "{} has written a {} {} novel which will {} both long-term fans and first time" \
             "readers.".format(author, second_adjectives, genre, feeling)

# ** Third Sentence **
third = "The writing style is {} and this makes the book {}.".format(writing_style, extra[0])

# ** Fourth Sentence **
fourth = "The underlying story is {} and which makes the ending {}.".format(extra[1], extra[2])

# ** Fifth Sentence Overall **

if recommend == "yes":
    recommend_it = "recommend"
else:
    recommend_it = "not recommend"

fifth = "Overall, I {} this book and would {} it to others.".format(overall, recommend_it)

# ** Sixth sentence - rating reason

sixth = "This is {} stars rounded {} {}".format(rating, up_down, reason)

review = [first, second, third, fourth, fifth, sixth]

for item in review:
    print(item)
