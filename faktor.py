# make factorial calculator 

def factorial(n):

    if n == 1:
        return 1

    elif n == 0:
        return 1

    else:
        for i in range(1, n):
            n = i * n
        return print(i + 1 , "factorial is: ", n)

factorial(2)