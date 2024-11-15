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
      