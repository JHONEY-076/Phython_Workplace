def main():
   
   triangle(3)
 
def triangle(size):
   
   for i in range(1,size+1):
      for j in range(-1*i+(size*1)):
         print(" ",end="")
      for h in range(i):
         print("*",end="")
      print()      
         
main()