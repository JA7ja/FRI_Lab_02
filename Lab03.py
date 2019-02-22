import random

def choose_word():
    word_file = open("C:\\Users\\IASA-FRI\\Desktop\\FRI Lab\\sowpods.txt", "r")
    words = []
    for line in word_file:
        words.append(line)
    word_file.close()
    return(random.choice(words))

def test_char(word, char, obs_word, chars_guessed):
    retList = []
    if char in word:
        for i in range(0, len(word)):
            if(char == word[i]):
                retList.append(char)
            else:
                retList.append(obs_word[i])
        return retList, True
    else:
        return obs_word, False

def print_list(word):
    for i in word:
        print(i + " ", end='')
    print("")

def end_game(obs_word, actual_word):
    if "_" in obs_word:
        print("You Lose!")
        print("The word you were trying to guess was: " + actual_word)
    else:
        print("You win!")

def main():
    hangman_word = choose_word().upper()
    word_letters = []
    errors_remaining = 6
    chars_guessed = []
    obs_word = []
    all_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for letter in hangman_word:
        obs_word.append("_")
        word_letters.append(letter.upper())
    print("Welcome to Hangman!")
    print_list(obs_word)
    while(errors_remaining > 0 or not "_" in obs_word):
        print("Guess your letter: ", end="")
        char_guess = input().upper()
        char_guess_good = False
        while(char_guess_good == False):
            if(len(char_guess) > 1):
                print("That guess isn't a letter! Guess again: ", end="")
                char_guess = input().upper()
            elif(char_guess not in all_letters):
                print("That guess isn't a letter! Guess again: ", end="")
                char_guess = input().upper()
            elif(char_guess in chars_guessed):
                print("You've already guessed that letter! Guess again: ", end="")
                char_guess = input().upper()
            else:
                char_guess_good = True
                chars_guessed.append(char_guess)
        guess_correct = test_char(hangman_word, char_guess, obs_word, chars_guessed)[1]
        if(not guess_correct):
            print("Incorrect!")
            errors_remaining = errors_remaining-1
            obs_word = test_char(hangman_word, char_guess, obs_word, chars_guessed)[0]
            if(errors_remaining == 1):
                print(str(errors_remaining) + " incorrect guess remaining")
                print_list(obs_word)
            else:
                print(str(errors_remaining) + " incorrect guesses remaining")
                print_list(obs_word)
        else:
            obs_word = test_char(hangman_word, char_guess, obs_word, chars_guessed)[0]
            print_list(obs_word)
    end_game(obs_word, hangman_word)

main()
