def play_hangman():
    print("*" * 29)
    print("Welcome to the Hangman game!")
    print("*" * 29)

    secret_word = "banana"
    hanged = False
    right = False

    while not hanged and not right:

        user_kick = input("What letter? ").strip()
        index = 0

        for letter in secret_word:

            if user_kick.upper() == letter.upper():
                print(f'Found the letter "{letter}" in position {index}')
            index += 1

        print("Playing...")

    print("*" * 29)
    print("End Game")


if __name__ == "__main__":
    play_hangman()
