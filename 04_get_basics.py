# Component 04 - Genre and other basic info from user

# Functions


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

# **Set up genre list and sort it**
genre_list = ["Action", "Adventure", "Detective", "Crime",
              "Fan-Fiction", "Anthology", "Mystery", "Science Fiction (Sci-Fi)",
              "Western", "Steam Punk", "Drama", "Horror", "Suspense", "Thriller",
              "Romance", "Chic Lit", "Humor", "Satire", "Classic", "Historical Fiction",
              "Realistic Fiction", "Narrative", "Biography", "Autobiography", "Memoir",
              "Comic", "Graphic Novel", "Fable", "Fairy Tale", "Fantasy", "Legend",
              "Magical Realism", "Mythology", "Short Story"]

genre_list.sort()


# Makes everything in the list lowercase
genre_list = [x.lower() for x in genre_list]

genre = text_helper("Please choose a genre", genre_list, 4, "yes")

print("Genre: '{}'".format(genre))
