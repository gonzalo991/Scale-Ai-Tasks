import random

def find_the_number(target, min=1, max=100):
    find = None
    attempts = 0
    while find != target:
        find = random.randint(min, max)
        attempts += 1
        user_answer = int(input(f"Attempt {attempts}: Guess the number between {min} and {max}: "))
        if user_answer == target:
            print("¡Congratulations! You've guessed the number.")
            print(f"The objective - {target_number} - was find after: {attempts} attempts.")
            break
        elif user_answer == find:
            print("¡Fantastic! You've guessed the randomly generated number. But this number isn't the objective.")
        else:
            print("Try it again.")
    return find

target_number = 20
found_number = find_the_number(target_number)


