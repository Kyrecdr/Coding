import random
print("GUESSING GAME PROGRAM")
print("From 1 to 100, you need to guess the correct number (you only get 10 chances)")
rnd = random.randint(1, 100)
count = 0
while True:
    guess = int(input("Guess the number between 1 to 100: "))
    count += 1
    if guess == rnd:
        print("Congrats! You correctly guessed the number", rnd)
        print("You guessed the number in", count, "tries")
        break;
    
    if guess < rnd:
        print("The number you guessed is too low, try again")
    else:
        print("The number you guessed is too high, try again")
        
    if count > 10:
        print("You've reached the maximum number of guesses")
        print("The random number is", rnd)
        break;