# Wordle Clone
# 1.27.2022
# Nicholas Bray

import random
testing = False


if __name__ == '__main__':
    # Import dictionary and choose random word
    dictFile = open('dict.txt')
    words = set()
    line = dictFile.readline()
    while line != '':
        words.add(line)
        line = dictFile.readline()
    wordOfTheDay = random.sample(words, 1)[0]
    if testing:
        print('For testing only - word:', wordOfTheDay)

    # Game Logic
    won = False
    guesses = 6
    hints = [' ', ' ', ' ', ' ', ' ']
    while (not won) and (guesses > 0):
        print('[' + hints[0] + '][' + hints[1] + '][' + hints[2] + '][' + hints[3] + '][' + hints[4] + ']')
        print(guesses, 'guesses remaining.')
        hints = [' ', ' ', ' ', ' ', ' ']
        guess = input('guess: ')
        guess.lower()
        if len(guess) != 5 or not guess.isalpha:
            print('Invalid guess')
        elif (guess+'\n') not in words:
            print('Guess not in dictionary')
        else:
            for letterIdx in range(5):
                if guess[letterIdx] == wordOfTheDay[letterIdx]:
                    hints[letterIdx] = 'G'
                elif guess[letterIdx] in wordOfTheDay:
                    hints[letterIdx] = 'Y'
            if hints == ['G', 'G', 'G', 'G', 'G']:
                won = True
            guesses -= 1
    if(won):
        print('You won!')
    else:
        print('You lost :(')
    input('Press any key to exit...')