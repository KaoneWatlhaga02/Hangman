# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist = load_words()

vowels= 'aeiou'

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    vowels= 'aeiou'
    n=0
    for i in secret_word:
        if i not in letters_guessed:
            break
        n += 1
    return n == len(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    get_guessed_word_list = []
    for i in secret_word:
        if i in letters_guessed:
            get_guessed_word_list += [i]
        else:
            get_guessed_word_list += ['_ ']
    get_guessed_word = ''.join(get_guessed_word_list)
    return get_guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    get_available_letters_list = []
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            get_available_letters_list += [i]
    get_available_letters = ''.join(get_available_letters_list)
    return get_available_letters
    
    

def hangman(secret_word, letters_guessed=None):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    secret_word = get_guessed_word(secret_word, letters_guessed)
    word_completion = '_' * len(secret_word)
    guessed = False
    letters_guessed = []
    limit = 6
    warnings = 3
    name = input("What is your name: ")
    print("Hello" + name + "lets play Hangman!")
    print("The length of your word is" + word_completion + "You have"+ limit +"tries and" + warnings + " left. Best of Luck!")

    while limit >= 1:
        print("You have", limit , "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        user_guess = input("Please guess a letter: ")

        if user_guess in secret_word and user_guess in get_available_letters(letters_guessed):
            letters_guessed += user_guess
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            if user_guess in string.ascii_lowercase and user_guess in get_available_letters(letters_guessed):
                letters_guessed += user_guess
                print("Oops! wrong letter, try again:", get_guessed_word(secret_word, letters_guessed))
                if user_guess in vowels:
                    limit = limit - 2
                else:
                    limit = limit - 1
            else:
                if limit > 0:
                    limit = limit - 1
                    if user_guess in letters_guessed:
                        print("Sorry! You have already guessed that letter. You now have", limit,
                              "warnings left. Try again.")
                    else:
                        print("Sorry again! That letter is invalid. You now have", warnings, "warnings left.")
                else:
                    limit = limit - 1
                    if user_guess in letters_guessed:
                        print("Oops! You have already guessed that letter. You now have", warnings,
                              "warnings left.")
                    else:
                        print("Invalid letter. You now have", warnings, "warnings left.")
        print("You lost!")

        if is_word_guessed(secret_word, letters_guessed):
            break

    unique_letters = ''.join(set(secret_word))
    unique_letters_length = len(unique_letters)
    score = limit * unique_letters_length
    score_string = str(score)
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won! Your score is:", score_string + ".")
    else:
        print("Sorry, you lost. The word was", secret_word + ".")


    hangman(secret_word)







# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    len_my_word = len(my_word.replace(" ", ""))
    len_other_word = len(other_word)

    other_list = list(other_word)

    my_list = list(my_word.replace(" ", "").replace("_", ""))
    if bool(my_list):
        if len_my_word == len_other_word:
            for counter in my_list:

                if my_list.count(counter) == other_list.count(counter):
                    if counter in other_list:
                        if [k for k, x in enumerate(list(my_word.replace(" ", ""))) if x == counter] == \
                                [k for k, x in enumerate(other_list) if x == counter]:
                            accuracy = True
                            continue
                        else:
                            accuracy = False
                            break
                    else:
                        accuracy = False
                        break
                else:
                    accuracy = False
                    break
        else:
            accuracy = False
    else:
        if len_my_word == len_other_word:
            accuracy = True
    return accuracy


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            possible_matches += [i]
    show_possible_matches = " ".join(possible_matches)

    if len(possible_matches) >= 1:
        return show_possible_matches
    else:
        return "No matches found"

    
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    letters_guessed = []
    limits = 6
    warnings = 3
    hints = 3

    print("Welcome to hangman!")
    print("A word that i am thinking of is", len(secret_word), "letters long.")
    print("------------")
    print("You have", warnings, "warnings left. Let's Begin!!!")

    while limits >= 1:
        print("You have", limits, "guesses left.")
        print("Remaining letters:", get_available_letters(letters_guessed))
        user_guess = input("Please guess a letter: ")

        if user_guess in secret_word and user_guess in get_available_letters(letters_guessed):
            letters_guessed += user_guess
            print("Good Job!:", get_guessed_word(secret_word, letters_guessed))

        elif user_guess == "*":
            if hints > 0:
                print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                hints = hints - 1
                print("You now have", hints, "hints left.")
            else:
                if warnings > 0:
                    warnings = warnings - 1
                    print("Oops! You have no remaining hints. You how have", warnings, "warnings left.")
                else:
                    limits = limits - 1
                    print("Sorry! You have no remaining hints and You are out of warnings, so you lose a guess.")

        else:
            if user_guess in string.ascii_lowercase and user_guess in get_available_letters(letters_guessed):
                letters_guessed += user_guess
                print("Sorry! Wrong letter:", get_guessed_word(secret_word, letters_guessed))
                if user_guess in vowels:
                    limits = limits - 2
                else:
                    limits = limits - 1
            else:
                if warnings > 0:
                    warnings = warnings - 1
                    if user_guess in letters_guessed:
                        print("Oops! You have already guessed that letter. You now have", warnings,
                              "warnings left.")
                    else:
                        print("Oops! Invalid letter. You now have", warnings, "warnings left.")
                else:
                    limits = limits - 1
                    if user_guess in letters_guessed:
                        print(
                            "Oops! You have already guessed that letter. You are out of warnings, so you lose a guess.")
                    else:
                        print("Oops! Invalid letter. You are out of warnings, so you lose a guess.")
        print("------------")

        if is_word_guessed(secret_word, letters_guessed):
            break

    unique_letters = ''.join(set(secret_word))
    unique_letters_length = len(unique_letters)
    score = limits * unique_letters_length
    score_string = str(score)
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won! Your score is:", score_string + ".")
    else:
        print("Sorry, you lost. The word was", secret_word + ".")


#secret_word = choose_word(wordlist)
#hangman_with_hints(secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = random.choice(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
