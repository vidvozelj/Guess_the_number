import random

secret_number = random.randint(0,9)
print('You have 3 tries to guess my secret number!!')
i = 0

while True:
    guess = input('Guess the number:')
    if guess.isdigit():
        i += 1
        guess_number = int(guess)
        if i <3:
            if guess_number == secret_number:
                print('Congratulations, you guessed the right number!!')
                break
            if guess_number != secret_number:
                print(f'You gueesed wrong! You have {3-i} more tries')
        else:
            print('Sorry, you are out of tries!!')
            break
    else:
        print('invalid input')

