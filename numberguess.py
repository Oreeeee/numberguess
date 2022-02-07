import random

hidden_number = random.randrange(10) + 1
failed_attempts = 0
usable_attempts = 3

print("Rules: You have to guess a random number between 1 and 10, and you have 3 chances. This program will tell you is this a bigger or smaller number.")

while failed_attempts < usable_attempts:
    user_input = int(input("Number: "))
    
    if user_input == hidden_number:
        print(f"Congratulations, you won! You had {attempts_left} attempts left.")
        break
    elif user_input > hidden_number:
        failed_attempts = failed_attempts + 1
        attempts_left = usable_attempts - failed_attempts
        print(f"The number is smaller. You have {attempts_left} attempt(s) left.")
        
    elif user_input < hidden_number:
        failed_attempts = failed_attempts + 1
        attempts_left = usable_attempts - failed_attempts
        print(f"The number is larger. You have {attempts_left} attempt(s) left.")
