import random

game_start = input("Do you want to start? Y/N")
if game_start == "Y".lower():
     random_number = random.randint(1, 100)
     attempts = 0
     while True:
        attempts = attempts + 1
        user_number = int(input("Guess the number:"))
        if user_number !=  random_number and random_number > user_number:
            print("too low!")
        elif user_number !=  random_number and random_number < user_number:
            print("too high!")
        elif user_number == random_number:
            print("Congratulations! That is the count of your tries:", attempts)
            break
else:
    print("Alright!")
