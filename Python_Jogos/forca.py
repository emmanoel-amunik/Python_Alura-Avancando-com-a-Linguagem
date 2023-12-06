def play_hangman():
    print("*" * 29)
    print("Welcome to the Hangman game!")
    print("*" * 29)

    secret_word = "banana"
    correct_letters = ["_", "_", "_", "_", "_", "_"]
    hanged = False
    right = False

    print(correct_letters)

    while not hanged and not right:

        user_kick = input("What letter? ").strip()
        index = 0

        for letter in secret_word:

            if user_kick.upper() == letter.upper():
                correct_letters[index] = letter
            index += 1

        print("Playing...", correct_letters)

    print("*" * 29)
    print("End Game")


if __name__ == "__main__":
    play_hangman()
