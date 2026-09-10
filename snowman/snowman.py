SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_IMAGE = [
    "*   *   *  ",
    " *   _ *   ",
    "   _[_]_ * ",
    '  * (")    ',
    "  \\( : )/ *",
    "* (_ : _)  ",
    "-----------",
]


def snowman(snowman_word):
    correct_letter_guess_statuses = build_letter_status_dict(snowman_word)
    wrong_guesses_list = []

    while True:
        print(generate_word_progress_string(snowman_word, correct_letter_guess_statuses))
        user_letter = get_letter_from_user(
            correct_letter_guess_statuses, wrong_guesses_list)

        if user_letter in correct_letter_guess_statuses:
            print(f"Correct! {user_letter} is in the word!")
            correct_letter_guess_statuses[user_letter] = True
        else:
            print(f"Sorry! {user_letter} isn't in the word!")
            add_wrong_letter(wrong_guesses_list, user_letter)

        if is_word_guessed(correct_letter_guess_statuses):
            # show a winning message along with the full word
            print(f"Congratulations, you win! The word was {snowman_word}")
            return

        print(build_snowman_graphic(len(wrong_guesses_list)))
        print_wrong_guesses_list(wrong_guesses_list)
        print_guesses_remaining(wrong_guesses_list)

        if len(wrong_guesses_list) == SNOWMAN_MAX_WRONG_GUESSES:
            # show a losing message along with the full word
            print(f"Sorry, you lose! The word was {snowman_word}")
            return


def build_snowman_graphic(wrong_guesses_count):
    """This function extracts a portion of the 
    snowman depending on the number of 
    wrong guesses and converts it to a single string
    """

    # get the part of the snowman for the number of wrong guesses
    lines = []
    for line_no in range(wrong_guesses_count):
        lines.append(SNOWMAN_IMAGE[line_no])

    return "\n".join(lines)


# There are no issues in this function
def get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif (user_input_string in correct_letter_guess_statuses 
                and correct_letter_guess_statuses[user_input_string]):
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string


def build_letter_status_dict(snowman_word):
    letter_status_dict = {}
    for letter in snowman_word:
        # keep track of any character a player might guess (alphabetic)
        if letter.isalpha():
            letter_status_dict[letter] = False

    return letter_status_dict


def is_word_guessed(correct_letter_guess_statuses):
    for guessed in correct_letter_guess_statuses.values():
        # if any letter hasn't been guessed, the word hasn't been guessed
        if not guessed:
            return False

    # all letters were guessed (or we'd have returned) so the word is guessed!
    return True


def generate_word_progress_string(snowman_word, correct_letter_guess_statuses):
    output_letters = []
    for elem in snowman_word:
        if not elem.isalpha(): 
            # add any non-alphabet characters
            output_letters += elem
        elif correct_letter_guess_statuses[elem]:
            # add any letters the player has guessed
            output_letters += elem
        else:
            # add a blank for any letter not yet guessed
            output_letters += "_"

            

    return " ".join(output_letters)


def add_wrong_letter(wrong_guesses_list, letter):
    # track the wrong guesses in alphabetical order
    wrong_guesses_list.append(letter)
    wrong_guesses_list.sort()


# There are no issues in this function
def print_wrong_guesses_list(wrong_guesses_list):
    if not wrong_guesses_list:
        return

    print(f"Wrong letters: {" ".join(wrong_guesses_list)}")


# There are no issues in this function
def print_guesses_remaining(wrong_guesses_list):
    if not wrong_guesses_list:
        return

    print(f"Wrong guesses left: {SNOWMAN_MAX_WRONG_GUESSES - len(wrong_guesses_list)}")
