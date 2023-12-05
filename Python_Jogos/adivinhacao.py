import random


def play_guessing():

    print("*" * 29)
    print("Welcome to the Guessing game!")
    print("*" * 29)

    total_attempts = 0
    secret_number = random.randrange(1, 101)
    score = 1000

    level = int(input("What level of difficulty?\n (1) Easy\n "
                      "(2) Medium\n (3) Hard\n  "))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    elif level == 3:
        total_attempts = 5

    for attempts in range(total_attempts):

        print(f"Attempt {attempts + 1} of {total_attempts}")
        user_kick = int(input("Type a number: "))

        if user_kick < 1 or user_kick > 100:
            print("You need to enter a number between 1 and 100")
            continue

        right = user_kick == secret_number
        greater = user_kick > secret_number
        less = user_kick < secret_number

        print(f"You entered: {user_kick}")

        if right:
            print(f"You're right!!! And your score is {score}")
            break
        else:
            if greater:
                print("You're wrong. Your guess was greater than the secret number.")
            elif less:
                print("You're wrong. Your guess was less than the secret number.")

            lost_points = abs(secret_number - user_kick)
            score -= lost_points

        print("*" * 60)

    print("End Game")


if __name__ == "__main__":
    play_guessing()
