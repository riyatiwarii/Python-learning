guess = 18
guess_count = 0
guess_limit = 8
while guess_count <= guess_limit:
    g = int(input("Enter guess\n"))
    guess_count = guess_count + 1
    if g < 18:
        print("Enter greater no.")
        print("Guesses left", 9 - guess_count)
    elif g > 18:
        print("Enter lesser no.")
        print("Guesses left", 9 - guess_count)
    elif g==18:
        print("You won")
        print("Guesses left", 9 - guess_count)
        break

else:
    print("No guess left" , 9 - guess_count)
    print("Game over")




