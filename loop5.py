# size=4
# 
# def main():
#    
#    draw_line()
#    draw_top()
#    draw_bottom()
#    draw_line()
#    
#    
# def draw_line():
#    print("#================#")
# 
# 
# def draw_top():
#      for line in range(1,size+1):
#       print("|", end="")
#       
#       for j in range(-2*line + (2*size)):
#          print(" ",end="")
#       
#       print("<>",end="")
#       
#       for k in range(4*line - 4):
#          print(".",end="")
#          
#       print("<>",end="")   
#       for a in range(-2*line + (2*size)):
#          print(" ",end="") 
#          
#       print("|")     
#  
#       
#       
# 
# 
# 
# def draw_bottom():
#    for line in range(1,size+1):
#       print("|", end ="")
#     
#       for i in range(2*line-2):
#          print(" ", end="")
#  
#       print("<>",end="")
#       
#       for j in range(-4*line+size*4):
#          print(".",end="")
#       
#       print("<>",end="")
#       
#       for k in range(2*line-2):
#          print(" ",end="")
#       
#       
#       print("|", end="")
#       
#       print()
# 
# 
# main()
#       


size=3

def main():
   draw_line()
   draw_top()
   draw_bottom()
   
   

def draw_line():
   print("#================#")
   
def draw_top():
   for line in range(1,size+1):
      print("|",end="")
      spaces()      
      print("<>",end="")
   
      for dot in range(4*line-4):
         print(".",end="")
      
      print("<>",end="")
      
      for space in range(-2*line+(2*size)):
         print(" ",end="")
         
      print("|",end="")   
         
         
      print()   
   

def draw_bottom():
   for line in range(1,size+1):
      print("|", end="")
      
      for space in range(2*line-2):
         print(" ",end="")
         
      print("<>",end="")
      
      for dot in range(-4*line+(size*4)):
         print(".",end="")
         
      print("<>",end="")
      
      spaces()      
      print("|",end="")   
         
      print()   
         
         
         
def spaces():
   for space in range(-2*line+(2*size)):
         print(" ",end="")





   
main()



# jusuck solved => ctrl+shift+/

# 
# def main():
#    draw_line()
#    draw_star_space()
#    draw_line()
#    
#    
#    
#    
# def draw_line():
#    print("************")
#    
#    
# def draw_star_space():
#    for i in range(5):
#       print("*",end="")
#       print(" "*10,end="")
#       print("*",end="")
#       print()
#         
# 
# 
# main()



