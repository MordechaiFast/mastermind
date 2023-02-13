'''Rules of Mastermind:
# The 'codemaker' chooses four pieces from six colors.
# At easy level, repeat colors are not allowed.
# At hard level, repeats and blanks are allowed.
# The 'codebreaker' guesses the four colors.
# The 'codemaker' reports how many pieces are in the correct position,
# and how many are a color that is present but not in the correct position.
'''

code = '1234'
guess = input('Make your guess: 'correct_position =     if guess_diget == code_dige    guess_digeguess_colors = set(guess    for guess_diget, code_diget in zip(guess, codecorrect_colors = guess_colors & code_colors - correct_positioprint(f'and {len(correct_colors)} others that are the right colors.'code_colors = set(codeprint(f'You have {len(correct_position)} in the right place,')
