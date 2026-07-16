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

    tries = 1
    max_tries = 7

    while guess!=secret and tries < max_tries:
        if guess > secret:
            print("The target number is smaller")
            guess=int(input("Try again: "))
        elif guess < secret:
            print("The target number is larger")
            guess=int(input("Try again: "))
            tries = tries + 1

    tries = tries + 1
    if guess != secret:
        print("Game Over! You used all your tries.")
        print("The correct number was:",secret)
    if guess == secret:
        print("Well done, your guess is correct.")
        print("Number of guesses: ",tries)
        if tries <= 3:
            print("⭐⭐⭐ excelent!")
        elif tries <= 6:
            print("⭐⭐ Good Job!")
        else:
            print("⭐ You Win!")
    play_again = input("Play again? (y/n): ").lower()