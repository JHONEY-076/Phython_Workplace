# 
# # add num 2
# sum=0
# for i in range(1,11):
#    print(sum)
#    sum+=i
#    
#    
# print("Cumulative sum:" ,sum)
# 
# 


# #2 to the 6th power
# base=2
# exp=6
# res=1
# for i in range(exp):
#    print(res)
#    res=res*base
# print(res)


# 
# sum=0
# for i in range(5):
#    sum+=int(input("Enter one number:"))
# print(sum)






#
# num=int(input("How mney people ate?"))
# result=0
# for i in range(1,num+1):
#    print("Person #",i,":",end="")
#    result+=float(input("How much did your dinner cost?"))
#    
# print()   
# print("Subtotal:",result)
# print("Tax",result*0.08)
# print("Tip",result*0.15)
# print("Total",result+(result)*0.15+(result)*0.08)
#    



# 
# 
# def main():
#    people=int(input("How mney people ate? "))
#    subtotal=0
#    for i in range(1,people+1):
#       print("Person #"+str(i)+":",end="")
#       print("How much did your dinner cost?",end="")
#       subtotal +=float(input())
#   print("subtotal:",subtotal)   
#    
#    
#    
#    
# main() 





# sum=""
# for i in range(ord("a"),ord("d")):
#    sum+=chr(i)
# print(sum)




# message= input("Your secret message:")
# key= int(input("Your secret key:"))
# 
# message=message.upper()
# 
# for i in range(len(message)):
#    
#    if message[i]>="A"and message[i]<="Z":
#       print(chr(ord(message[i])+key),end="")   
#    
#       if message[i]>"Z":
#          print(chr(ord(message[i]%ord("[")+ord("A"))))
# 
#    else:
#       print(" ",end="")
#       
#    
#    

# 
# text=input("Your secret message:?")
# key=int(input("Your secret key?:"))
# text=text.upper()
# 
# for letter in text:
#    if letter>= "A" and letter<="Z": 
#       shifted_num=ord(letter)+key
#       if shifted_num>ord("Z"):
#          shifted_num=shifted_num%ord('[')+ord('A')
#       print(chr(shifted_num),end="")
#    else:
#       print(letter, end="")
# 
#



# text=input("Your secret message:")
# key=int(input("Your secret key:"))
# 
# text=text.upper()
# 
# for letter in text:
#    if letter>="A"and letter<="Z":
#       shifted_letter=ord(letter)+key
#       if shifted_letter>ord("Z"):
#          shifted_letter=shifted_letter%ord("[")+ord("A")
#       if shifted_letter<ord("A"):
#          shifted_letter=ord("Z")-ord("@")%shifted_letter      
#       print(chr(shifted_letter),end="")    
#    else:
#       print(" ",end="")       
#        