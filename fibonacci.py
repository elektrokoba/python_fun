# Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1

def fibonacci(n): 
    if n<0: 
        print("Incorrect number") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2) 
  
print(fibonacci(10)) 