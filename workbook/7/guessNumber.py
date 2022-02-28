import random
def getInput():
    validInput = False
    while not validInput:
        number = input("Enter a number: ")
        if number.isnumeric():
            validInput = True
    return int(number)

def guessGame():
    compNo = random.randint(1,100)
    correctAnswer = False
    while not correctAnswer:
        guess = getInput()
        if guess == compNo:
            print("Correct answer!")
            correctAnswer = True
        elif guess > compNo:
            print("Too high!")
        elif guess < compNo:
            print("Too low!")

guessGame()
    
