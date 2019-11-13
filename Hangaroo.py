import string
lowercase = string.ascii_lowercase
print ("To start the game, give a word by typing the function: hangaroo('*yourword*')")
def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for i, c in enumerate(secretWord):
    	if c in lettersGuessed:
    		count += 1
    if count == len(secretWord):
    	return True
    else:
    	return False
def getGuessedWord(secretWord, lettersGuessed):
    result = []
    for i in secretWord:
        if i in lettersGuessed:
            result.append(i)
        else:
            result.append('_')
    return ' '.join(result)
def getAvailableLetters(lettersGuessed):
    remain = []
    for i in lowercase:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)
def hangaroo(secretWord):
    print('Welcome to Hangaroo!')
    print('Here is the word! It is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []

    while 5 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('CONGRATULATIONS! You win!')
            break
        else:
        	print('------------')
        	print('You have', 5 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Give a letter: ')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Good Job!: ', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Letter already given, pick another one.", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("That letter is not in the word, pick another one.", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 5 - mistakesMade == 0:
        	print('------------')
        	print('You lost! The word was', secretWord)
        	break
        else:
        	continue
