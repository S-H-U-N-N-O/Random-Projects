import random as Ishan

guesses = 1
var1 = Ishan.randint(1,100)
print("Hey I am Tobor. I am choosing a number between 1-100")
guess = int(input("Guess my chosen number: "))

while guess != var1:
    if guess > var1:
        print("Too high bro. -_-")
        guess = int(input("Guess again: "))
        guesses = guesses + 1
    elif guess < var1:
        print("Too low bro. -_-")
        guess = int(input("Guess again: "))
        guesses = guesses + 1

print("Congo, You have guessed the number in ",guesses," guesses.")