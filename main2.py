def main():
   line()
   content()
   line()
   

def line():

   print("+",end="")
   for i in range(10):
      print("-",end="")
   
   print("+")



def content():
   for i in range(1,6):
      print("|",end="")
      
      for j in range(1*i-1):
         print(" ",end="")
      
      print("\\",end="")      
         
      for n in range(1,-2*i+11):
         print(n,end="")
      
      print("/",end="")
      
      for j in range(1*i-1):
         print(" ",end="")
      
      
         
      print("|")   
      print()
      
      
      
      
      
main()