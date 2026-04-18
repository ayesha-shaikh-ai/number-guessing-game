import random

print("=== Number Guessing Game ===")
print("Select Difficulty:")
print("1. Easy (10 attempts)")
print("2. Medium (7 attempts)")
print("3. Hard (5 attempts)")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    attempts = 10
elif choice == "2":
    attempts = 7
else:
    attempts = 5

number = random.randint(1, 100)

for i in range(attempts):
    guess = int(input("Guess a number (1-100): "))

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"Correct! You guessed in {i+1} attempts.")
        break
else:
    print(f"You lost! The number was {number}")