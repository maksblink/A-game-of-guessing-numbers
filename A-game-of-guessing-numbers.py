from random import randint

secret_num = randint(1, 100)
while True:
    try:
        """Get number from user.

        Try until user give proper number.

        :rtype: float
        :given number as float
        """
        guess = float(input("Guess the number: "))
        """Main function with game."""
        if guess < secret_num:
            print("Too small!")
        elif guess > secret_num:
            print("Too big!")
        else:
            print("You win!")
            break
    except ValueError as ve:
        print("It's not a number!", ve)
