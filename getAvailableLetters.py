import string
lowercase = string.ascii_lowercase
def getAvailableLetters(lettersGuessed):
    remain = []
    for i in lowercase:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)