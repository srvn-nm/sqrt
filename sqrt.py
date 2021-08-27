num = int(input('enter your number: '))
guess = round(num / (num-1) , 10)
i = 0
while i <= 20000 :
    guessNum = round(num / guess , 10)
    newGuess = round((guess + guessNum) / 2 , 10)
    i += 1
    if newGuess == guess :
        break
    else :
        guess = newGuess
print(guess)