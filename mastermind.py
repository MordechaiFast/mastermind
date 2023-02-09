# Rules of Mastermind:
# The 'codemaker' chooses four pieces from six colors, or blank.
# The 'codebreaker' guesses the four colors.
# The codemaker reports how many pieces are in the correct position,
# and how many are a color that is present but not in the correct position.

code = '1234'
guess = input('Make your guess: ')
if guess == code:
    print('right')
else:
    print('wrong')
