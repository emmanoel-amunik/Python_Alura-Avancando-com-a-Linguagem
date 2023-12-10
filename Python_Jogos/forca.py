import random


def play_hangman():

    intro_msg()
    secret_word = load_secret_word()
    correct_letters = list_right_letters(secret_word)
    print(correct_letters)

    hanged = False
    right = False
    errors = 0

    while not hanged and not right:

        user_kick = input("What letter? ").strip().upper()

        if user_kick in secret_word:
            save_correct_kick(secret_word, user_kick, correct_letters)
        else:
            errors += 1
            drawn_hang(errors)

        hanged = errors == 7
        right = "_" not in correct_letters

        print("Playing...", correct_letters)

    print("*" * 29)

    if right:
        print_you_won()
    else:
        print_you_lose(secret_word)

    print("End Game")


def intro_msg():
    print("*" * 29)
    print("Welcome to the Hangman game!")
    print("*" * 29)


def load_secret_word():
    with open("words.txt") as file:
        words = []
        for line in file:
            words.append(line.strip())

    """file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)"""

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def list_right_letters(word):
    return ["_" for letter in word]


def save_correct_kick(secret_word, user_kick, correct_letters):
    index = 0
    for letter in secret_word:
        if user_kick == letter:
            correct_letters[index] = letter
        index += 1


def print_you_won():
    print("Congrats, you WON the game!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_you_lose(secret_word):
    print("Wow, you get hanged!!")
    print(f"The secret word was {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def drawn_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play_hangman()
