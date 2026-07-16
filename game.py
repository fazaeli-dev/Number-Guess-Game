import random
play_again = "y"
while play_again == "y":
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty == "easy":
        secret = random.randint(1,50)
    elif difficulty == "medium":
        secret = random.randint(1,100)
    elif difficulty == "hard":
        secret = random.randint(1,200)
    else:
        print("Invalid choice. Medium selected.")
        secret = random.randint(1,100)

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