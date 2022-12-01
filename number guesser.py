import random

upper_bound = int(input("Type a number: "))
attempt = 0

if upper_bound <= 0:
    print("Please type a number larger than 0 next time.")
    quit()

random_number = random.randint(0, upper_bound)
while True:
    user_guess = int(input("Make a guess: "))

    if user_guess == random_number:
        print("You got it right!")
        attempt += 1
        print("attempts: ", attempt)
        break
    elif user_guess > random_number:
            print("You were above the number")
            attempt += 1

    else:
        print("You were below the number")
        attempt += 1
        continue
    