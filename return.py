import random


def fun():
   for i in range(1,11):
       r=random.randint(1,10)
       print(str(r)+" ",end="")
       if r ==7:
         return r
    
      
fun()      
   