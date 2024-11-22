def print_num_range (num1,num2):
    
    print("[",end="")
    
    if num1>num2:
      for i in range(num1,num2,-1):
         print(i,end="")
         print(", ",end="")

      print(num2,end="")
      print("]")
      
    elif num1<num2:
         for i in range(num1, num2,1):
            print(i,end="")
            print(", ",end="")
      
         print(num2,end="")
         print("]")

      
    else: 
         
         print(num1)
         print("]")
         
   
print(print_num_range(2,7))   



