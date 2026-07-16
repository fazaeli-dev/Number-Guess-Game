import random
play_again = "y"
while play_again == "y":
    secret = random.randint(1, 100)

    guess=int(input("Find the target number: "))

    tries = 0

    while guess!=secret:
        tries = tries + 1
        if guess > secret:
            print("The target number is smaller")
            guess=int(input("Try again: "))
        elif guess < secret:
            print("The target number is larger")
            guess=int(input("Try again: "))

    tries = tries + 1
    print("Well done, your guess is correct.")
    print("Number of guesses: ",tries)
    play_again = input("Play again? (y/n): ").lower()