import random
print("Guessing Number game")
number = random.randint(1,9)
chance = 0
print("Guess a number between 1-9")

while chance<5:
    guess= int(input("Enter your guess"))
    if (guess == number):
        print("congralutaion!! you guessed right")
        break
    elif(guess<number):
        print("Guess is low: guess higher than",guess)
    else:
        print("Guess is high: guess lower than",guess)
chance+=1

if(not chance<5):
    print("You lose, the number was",number)






    