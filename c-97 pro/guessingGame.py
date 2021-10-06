import random

number=[1,2,3,4,5,6,7,8,9]
print(random.sample(number,k=1))
print("NUMBER GUESSING GAME")
print("guess a number from 1-9 :")
guess=input("enter your guess :")
if guess < number:
    print("Your guess was too low: Guess a number higher than",guess)
if guess > number:
    print("Your guess was too high: Guess a number lower than",guess)
