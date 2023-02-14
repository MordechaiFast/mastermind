'''Rules of Mastermind:
# The 'codemaker' chooses four 'pieces' from six 'colors'.
# At easy level, repeat colors are not allowed.
# At hard level, repeats and blanks are allowed.
# The 'codebreaker' guesses the four colors.
# The 'codemaker' reports how many pieces are in the correct position,
# and how many are a color that is present but not in the correct position.
'''

from random import randint


level = 0
num_of_guesses = 8
#code = '1234'
if level != 0:
    code = [randint(0 if level == 2 else 1, 6) for _ in '----']
else:
    code = []
    for _ in '----':
        while (digit := randint(1, 6)) in code:
            pass
        code.append(digit)
for guess_num in range(1, num_of_guesses + 1):
    guess = input(f'Guess #{guess_num}: ')
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
    print('*' * correct_digits + '-' * missplaced_digits)
    if correct_digits == 4:
        break
if correct_digits != 4:
    print(code[0], code[1], code[2], code[3], sep='')
