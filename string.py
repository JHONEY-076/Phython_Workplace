import math

def caesar_cipher():
   message=input("Your message? ")
   key=int(input("Encoding key? "))
   
   message=message.upper()
   
   for letter in message:
      if letter>="A" and letter<="Z":
         shifted_num=ord(letter)+key
         if shifted_num>ord("Z"):
            shifted_num=shifted_num%ord("[")+ord("A")
         elif shifted_num<ord("A"):
            shifted_num=ord("Z")-shifted_num%ord("@")
            
         print(chr(shifted_num),end="")      
              
      
      else:
         print(letter,end="")       
                 
caesar_cipher()       