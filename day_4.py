##Day-4

def is_prime():
    for num in range(0, 100 + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num)  
is_prime()
