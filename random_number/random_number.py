import random


def main():
    print("Welcome to Guess the Number")
    print("---------------------------")
    counter = 0
    rnd = random.randint(1, 100)
    base_rnd = random.randint(2,16)
    counter = guess_number(rnd,base_rnd)
    print(f"Tries: {counter}")

def guess_number(random_number,base_number):
    print(f"{random_number}")
    counter = 0
    while counter < 3:
        user_input = input(f"Number(base: {base_number}) ").strip()
        if not user_input.isdigit():
            print(f'Please input integer not string...')
            continue 
        
        counter += 1
        if int(user_input,base_number) == random_number:
            print(f"You guess the correct number: {random_number}. Number of tries {counter}")
            return counter 
        elif int(user_input,base_number) > random_number:
            print(f"Number too high. Try again...Tries:{counter}")
        elif int(user_input,base_number) < random_number:
            print(f"Number too low. Try again...Tries: {counter}")
        else:
            print("Wrong Type...")
        if counter == 3:
            print(f"Sorry... you had already {counter} tries...")
            return counter

if __name__ == "__main__":
    main()
