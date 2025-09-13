import random
secret_number = random.randint(1,100)
attempts = 0
print("welcome to the guessing game, its time to test youre intuition")
print("🤔mmmm, Lets think of a number between 1 and 100")
while True:
    guess = input("Take a guess: ")

    if not guess.isdigit():
        print("please enter a valid numbe.")
        continue
    guess = int(guess)
    attempts += 1
     
    if guess < secret_number - 10:
        print("Too low! guess again")
    elif guess < secret_number:
        print("close! guess a bit higher")
    elif guess > secret_number + 10:
        print("Too high! try again")    
    elif guess > secret_number:
        print("close! guess a bit lower")
           

    else:
        print(f"CONGRATULATIONS you guessed it in {attempts} attempts")  
        break 
           