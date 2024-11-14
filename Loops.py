import random
print ("Welcome to the Guessing game!")
print ("Please guess a number between 1 & 10. I will tell if you have guessed correctly")

guess = 0
num = random.randint(1,10)

while guess != num:
    guess = int(input())
    if guess < num:
        print("higher")
    elif guess > num:
        print("lower")
    else:
        print("You have guessed the correct number")
print("Shanks for playing")