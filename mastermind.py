'''Rules of Mastermind:
# The 'codemaker' chooses four 'pieces' from six 'colors'.
# At easy level, repeat colors are not allowed.
# At hard level, repeats and blanks are allowed.
# The 'codebreaker' guesses the four colors.
# The codemaker reports how many pieces are in the correct position,
# and how many are a color that is present but not in the correct position.
'''

from random import randint


level = 0
num_of_guesses = 8
if level != 0:
    code = [randint(0 if level == 2 else 1, 6) for _ in '----']
else:
    code = []
    for _ in '----':
        while (diget := randint(1, 6)) in code:
            pass
        code.append(diget)
for guess_num in range(1, num_of_guesses + 1):
    guess = input(f'Guess #{guess_num}: ')
    correct_digets, missplaced_digets = 0, 0
    incorrect_guess_digets, unguessed_code_digets = [], []
    for guess_diget, code_diget in zip(guess, code):
        if guess_diget == code_diget:
            correct_digets += 1
        else:
            incorrect_guess_digets.append(guess_diget)
            unguessed_code_digets.append(code_diget)
    for guess_diget in incorrect_guess_digets:
        for code_diget in unguessed_code_digets:
            if guess_diget == code_diget:
                missplaced_digets += 1
                del code_diget
                break
    print('*' * correct_digets + '-' * missplaced_digets)
    if correct_digets == 4:
        break
if [diget for diget in guess] != code:
    print(diget for diget in code)
