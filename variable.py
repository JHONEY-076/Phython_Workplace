<<<<<<< HEAD
# def print_design():
# 
#    for i in range(1, 10, 2):
#     spaces = (11 - i) // 2 
#     print('-' * spaces + str(i) * i + '-' * spaces)
# 
# 
# 
# print_design()


for i in range(1,6):
   
   for j in range(-1*i+6):
        print("-",end="")
      
   for n in range(2*i-1):
      print(2*i-1,end="")   
     
   for j in range(-1*i+6):
        print("-",end="")
 
   print()
      
=======
HEIGHT=4


for i in range(1,HEIGHT+1):
   for j in range(i-1):
      print("          ",end="")
   print("+=========+")
   for j in range(i-1):
      print("          ",end="")
   print("+=========+")
   for j in range(i-1):
      print("          ",end="")
   print("+=========+")
      

   for i in range(1, 10, 2):
    spaces = (11 - i) // 2 
    print('-' * spaces + str(i) * i + '-' * spaces)



print_design()


>>>>>>> 518227eaaa92e1a074324f5f88704a167423e347
