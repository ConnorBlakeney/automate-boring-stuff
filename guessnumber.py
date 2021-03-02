import random 

print("Hello, what is your name?")
name = input()

secret_num = random.randint(1, 20)

print(name + ", I am thinking of a number between 1 and 20. You will have 5 attempts to guess my number.")

for guessesTaken in range(1, 6):
    print("Take a guess!")
    guess = int(input())
    if guess < secret_num:
        print("Your guess is too low.")
    elif guess > secret_num: 
        print("Your guess is too high.")
    else: 
        break

if guess == secret_num:
    print(name + ", you guessed the correct number in " + str(guessesTaken) + " attempts. Great job!")
else: 
    print("Nope. The number I was thinking of was: " + str(secret_num) + ".")