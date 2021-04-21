from random import randint

secret_num = randint(1, 100)
while True:
    try:
        guess = float(input("Guess the number: "))
        if guess < secret_num:
            print("Too small!")
        elif guess > secret_num:
            print("Too big!")
        else:
            print("You win!")
            break
    except ValueError as ve:
        print("It's not a number!", ve)
