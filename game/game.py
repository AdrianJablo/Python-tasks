import random

while True:
    try:
        level = int(input("Level: "))
        number = random.randint(1, level)
        break
    except (SyntaxError,ValueError):
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
           print("Just right!")
           break
    except (SyntaxError,ValueError):
        pass
