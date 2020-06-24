# make factorial calculator 

def factorial(inputNumber):

    if isinstance(inputNumber, int):

        if inputNumber == 0:
            return 1
        
        elif inputNumber < 0:
            return None

        else:
            for i in reversed(range(1, inputNumber)):
                inputNumber = i * inputNumber
                print(inputNumber)
            return inputNumber
    
    else:
        return None

       
print(factorial(-3))
