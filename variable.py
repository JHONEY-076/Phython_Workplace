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


