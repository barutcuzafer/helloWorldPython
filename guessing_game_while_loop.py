real_number=9
guessCounter=0
guessLimit=3

while guessCounter<guessLimit:
    guess = int(input('Guess: '))
    guessCounter+=1
    if guess == real_number:
        print("You won")
        break
else:
    print("Sorry, you failed")





