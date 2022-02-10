import random


def main():
    hidden_number = random.randint(1, 10)
    failed_attempts = 0
    usable_attempts = 3
    attempts_left = usable_attempts

    print("Rules: You have to guess a random number between 1 and 10, and you have 3 chances. This program will tell you is this a bigger or smaller number.")

    while failed_attempts < usable_attempts:
        while True:
            try:
                user_input = int(input("Number: "))
                if user_input > 10 or user_input < 1:
                    print("You have to enter a number between 1 and 10")
                else:
                    break
            except ValueError:
                print("You have to enter a number!")
        failed_attempts = failed_attempts + 1
        if user_input == hidden_number:
            print(f"Congratulations, you won! You had {attempts_left} attempt(s) left.")
            break
        elif user_input > hidden_number:
            attempts_left = usable_attempts - failed_attempts
            print(f"The number is smaller. You have {attempts_left} attempt(s) left.")
        elif user_input < hidden_number:
            attempts_left = usable_attempts - failed_attempts
            print(f"The number is larger. You have {attempts_left} attempt(s) left.")
        if attempts_left == 0:
            print("You lose!")
            break


if __name__ == '__main__':
    main()
