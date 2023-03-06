'''Rules of Mastermind:
# The 'codemaker' chooses four 'pieces' from six 'colors'.
# At easy level, repeat colors are not allowed.
# At hard level, repeats and blanks are allowed.
# The 'codebreaker' guesses the four colors.
# The 'codemaker' reports how many pieces are in the correct position,
# and how many are a color that is present but not in the correct position.
'''

from random import randint


def produce_code(level = 0) -> list:
    '''Generates a random four diget code, according to the Mastemind rules
    
    >>> import random
    >>> random.seed(0)
    >>> produce_code()
    [4, 1, 3, 5]
    >>> produce_code(level=1)
    [4, 4, 3, 4]
    >>> random.seed(2)
    >>> produce_code(level=2)
    [6, 6, 0, 0]
    '''
    
    if level != 0:
        code = [randint(0 if level == 2 else 1, 6) for _ in '----']
    else:
        code = []
        for _ in '----':
            while (digit := randint(1, 6)) in code:
                pass
            code.append(digit)
    return code

def score_guess(guess, code):
    '''Scores a guess against a given code.
    Allows the guess or the code to be given as a string or list of ints.
    Returns the number of places that are correct, and the number of places
    that are present but not correct
    '''
    correct_digits, missplaced_digits = 0, 0
    incorrect_guess_digits, unguessed_code_digits = [], []
    for guess_digit, code_digit in zip(guess, code):
        if int(guess_digit) == int(code_digit):
            correct_digits += 1
        else:
            incorrect_guess_digits.append(guess_digit)
            unguessed_code_digits.append(code_digit)
    for guess_digit in incorrect_guess_digits:
        for code_digit in unguessed_code_digits:
            if int(guess_digit) == int(code_digit):
                missplaced_digits += 1
                del code_digit
                break
    return correct_digits, missplaced_digits

num_of_guesses = 8

def main():
    '''The flow function for the game.
    Includes set-up and end game.
    '''
    # Set up
    code = produce_code()
    # Turn loop
    for guess_num in range(1, num_of_guesses + 1):
        # Receive a guess
        while ( # Validate guess format
            not (guess := input(f'Guess #{guess_num}: ')).isdecimal()
            or len(guess) != 4
        ):
            print('Enter four digits')
        # Score the guess
        correct, missplaced = score_guess(guess, code)
        # Report the score
        print('*' * correct + '-' * missplaced)
        # Check for a win
        if correct == 4:
            break
    # End game: reveal the code
    print(code[0], code[1], code[2], code[3], sep='')

if __name__ == '__main__':
    main()
