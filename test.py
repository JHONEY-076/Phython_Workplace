SIZE=5

def main():
  
   draw_top()
   draw_line()
   draw_body()
   draw_line()
   draw_body2()
   draw_line()
   draw_top()
   
def draw_top():
   
   for i in range(1,SIZE*2):
      for j in range(-1*i+(SIZE*2)):
         print(" ",end="")
         
      for k in range(1*i):
         print("/",end="")
         
      
      print("**",end="")
            
      for a in range(1*i):
         print("\\",end="")
         
      print()


def draw_line():
      print("+",end="")
      for i in range(SIZE*2):  
         print("=*",end="")
              
      print("+")   

def draw_body():
   for i in range(1,SIZE+1):
      print("|",end="")
      for dot in range(-1*i+(SIZE)):
         print(".",end="")
      for slash in range(i):
         print("/\\",end="")
      for dots in range(-2*i+(SIZE*2)):
         print(".",end="")
      for slash2 in range(i):
         print("/\\",end="")
      for dots in range(-1*i+(SIZE)):
         print(".",end="")
      print("|", end="")   
      print()   
         
   for i in range(1,SIZE+1):
       print("|",end="")
       for dot in range(1*i-1):
          print(".",end="")
       for slash in range(-1*i+(SIZE+1)):
          print("\\/",end="")
       for dots in range(2*i-2):
          print(".",end="")
       for slash2 in range(-1*i+(SIZE+1)):
          print("\\/",end="")
       for dots in range(1*i-1):
          print(".",end="")
       print("|", end="")   
       print()   
            
                  
            
def draw_body2():
   for i in range(1,SIZE+1):
       print("|",end="")
       for dot in range(1*i-1):
          print(".",end="")
       for slash in range(-1*i+(SIZE+1)):
          print("\\/",end="")
       for dots in range(2*i-2):
          print(".",end="")
       for slash2 in range(-1*i+(SIZE+1)):
          print("\\/",end="")
       for dots in range(1*i-1):
          print(".",end="")
       print("|", end="")   
       print()   

   for i in range(1,SIZE+1):
      print("|",end="")
      for dot in range(-1*i+(SIZE)):
         print(".",end="")
      for slash in range(i):
         print("/\\",end="")
      for dots in range(-2*i+(SIZE*2)):
         print(".",end="")
      for slash2 in range(i):
         print("/\\",end="")
      for dots in range(-1*i+(SIZE)):
         print(".",end="")
      print("|", end="")   
      print()

                     
      

main()