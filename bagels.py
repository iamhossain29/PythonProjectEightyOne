import random

num_digits = 4
max_guess = 5


def main():
    print('''Bagels, A deductive logic game''')

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(max_guess))

        numGuesses = 1
        while numGuesses <= max_guess:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            #numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guess:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        print('Do you want to play again? {Yes or no}')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()

################################################

# 1. What happens when you change the NUM_DIGITS constant? NUM_DIGITS sets the length of the gussed number, so changing NUM_DIGITS will change the length of the guessed number
# 2. What happens when you change the MAX_GUESSES constant? this  variable the sets the maximum guess one player can get, setting it to a higher value will increase the guess number.
# 3. What happens if you set NUM_DIGITS to a number larger than 10? it will make the guessed number length to 10
# 4. What happens if you replace secretNum = getSecretNum() on line 30 with secretNum = '123'? it will set the secret number to 123 and it will match player guess with this number
# 5. What error message do you get if you delete or comment out numGuesses = 1 on line 34? UnboundLocalError: local variable 'numGuesses' referenced before assignment
# 6. What happens if you delete or comment out random.shuffle(numbers) on line 62? it will tale 0123 from the list as secret number
# 7. What happens if you delete or comment out if guess == secretNum: on line 74 and return 'You got it!' on line 75? it will not print You got it! if the player guess the seret nubmer right
# 8. What happens if you comment out numGuesses += 1 on line 44? it wont increse numguess variable, it wont stop the game continously it will continue with guess#1
#
#
#
#
#
#
#
#
#
#
#
#
#