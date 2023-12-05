import forca
import adivinhacao


def choose_game():
    msg = "Choose your game!"
    size = len(msg) + 12

    print("*" * size)
    print("*" * 5, f"{msg}", "*" * 5)
    print("*" * size)

    user_choice = int(input("Which game? \n(1) Hang man \n(2) Guessing\n "))

    if user_choice == 1:
        print("Playing hangman")
        forca.play_hangman()

    elif user_choice == 2:
        print("Playing guessing")
        adivinhacao.play_guessing()


if __name__ == "__main__":
    choose_game()
