'''Rules of Mastermind:
# The 'codemaker' chooses four pieces from six colors.
# At easy level, repeat colors are not allowed.
# At hard level, repeats and blanks are allowed.
# The 'codebreaker' guesses the four colors.
# The codemaker reports how many pieces are in the correct position,
# and how many are a color that is present but not in the correct position.
'''

code = '1234'
guess = input('Make your guess: ')
#sets might only work for easy level...
correct_position = {
    guess_diget
    for guess_diget, code_diget in zip(guess, code)
    if guess_diget == code_diget
}
correct_colors = set(guess) & set(code) - correct_position
if len(correct_position) == 4:
    print('Right')
else:
    print(f'You have {len(correct_position)} in the right place,')
    print(f'and {len(correct_colors)} others that are the right colors.')
