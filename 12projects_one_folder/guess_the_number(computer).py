import random 


def guess(x = 10, y = 10):
    random_number = random.randint(1, x)
    guess = 0 
    tries = y

    while guess != random_number and tries != 0:
        guess = int(input(f"guess a number between 1 and {x}"))
        if guess < random_number:
            print("sorry, guess again. too low")
        elif guess > random_number:
             print("sorry, guess again. too high")
        tries = tries - 1
    if guess == random_number: 
        print(f"congrats, you have guessed the number!")
    else:
        print(f"Your {y} tries have run out!")

guess(100, 10)