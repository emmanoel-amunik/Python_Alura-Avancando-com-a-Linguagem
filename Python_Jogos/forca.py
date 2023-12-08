import random


def play_hangman():
    print("*" * 29)
    print("Welcome to the Hangman game!")
    print("*" * 29)

    with open("words.txt") as file:
        words = []
        for line in file:
            words.append(line.strip())

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    correct_letters = ["_" for letter in secret_word]

    hanged = False
    right = False
    errors = 0

    print(correct_letters)

    while not hanged and not right:

        user_kick = input("What letter? ").strip().upper()

        if user_kick in secret_word:

            index = 0
            for letter in secret_word:

                if user_kick == letter:
                    correct_letters[index] = letter
                index += 1
        else:
            errors += 1

        hanged = errors == 6
        right = "_" not in correct_letters

        print("Playing...", correct_letters)

    print("*" * 29)

    if right:
        print("You won the game!!!")
    else:
        print("You lose the game!")

    print("End Game")


if __name__ == "__main__":
    play_hangman()
