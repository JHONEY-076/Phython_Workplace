# sum=0
# response = input("Type a word (or \"quit\" to exit): ") # post
# 
# while (response!="quit"):
#    sum+= len(response)
#    response=input("Type a word (or \"quit\" to exit): ") # post
#    
# print("You typed a total of",str(sum),"characters")   
# 
# 



# import random
# 
# def main():
#   num1=random.randint(1,6)
#   num2=random.randint(1,6)
#   sum=num1+num2
#   print(str(num1)+"+"+str(num2)+"="+str(sum))
#   count=1
#   
#   while(sum!=7):
#    num1=random.randint(1,6)
#    num2=random.randint(1,6)
#    sum=num1+num2
#    print(str(num1)+"+"+str(num2)+"="+str(sum))
#    count+=1
#    
#   print("You won after",count,"tries!")
#   
#   
#   
# main()
# 
# 

import random

def main():
   i=random.randint(2,5)
   
   num=random.randint(1,10)
   print(str(num),end="")
   
   for j in range(i):   
     num=random.randint(1,10)
     print("+",end="")
     print(str(num),end="")
   print("=",end="")
           
     






main()