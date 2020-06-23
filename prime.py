num = 200

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"not prime")
           break
   else:
       print(num,"prime")      
else:
   print(num,"not prime")