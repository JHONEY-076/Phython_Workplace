def name_diamond(name):
       
   for j in range(len(name)):
      print(name[ :j+1])

   for i in range(1,len(name)):
      for j in range(i):
         print(" ",end="")
      print(name[i:])
    
name_diamond("MARTY")