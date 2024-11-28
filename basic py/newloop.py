import random
rnum = random.randint(1, 10)
max_attempts = 5
guess = 0
print("Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess a number between 1 and 10.")
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    if guess < rnum:
        print("higher")
    elif guess > rnum:
        print("lower")
    else:
        print("Correct")
        break
else:
    print("Attempts Exhausted")