print("Make up a number from 0 to 1000 and I'll guess it in 10 moves max.")
max = 1001
min = -1
while True:
    guess = int((max - min) / 2) + min
    print("I guess: " + str(guess))
    ans = input("1 - too big\n2 - too small\n3 - you win\n")
    if (ans != "1") and (ans != "2") and (ans != "3"):
        print("Invalid input.")
    if ans == "3":
        print("I won!")
        break
    elif ans == "1":
        max = guess
    elif ans == "2":
        min = guess
    if abs(max - min) <= 1:
        print("Don't cheat on me!")
