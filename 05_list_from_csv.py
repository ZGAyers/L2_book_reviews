# Component 05 - Get adjectives from csv file and sort

# Functions:


# Make a list function
def make_list(file_name):
    file_name = file_name+".txt" # add .txt to names to make it easier to call
    list_name = open(file_name).read().splitlines()
    return list_name


# Genre picker function
def text_helper(question, possible_answers, items_per_line, required=None):
    error = "This is a required field. Please choose an item from the list" \
            "or type in a word / phrase"
    print(question)

    valid = False
    while not valid:

        # Output numbered list with specified number of items per line
        count_ans = 0

        for item in possible_answers:
            print("{}. {}".format(possible_answers.index(item)+1, item),
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


# --main routine--

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

# Test that list had been generated
genre = "action"
adjective = text_helper("Choose an adjective", "yes", 4, action_list)
print(adjective)
