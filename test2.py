def main():
   full_name = input("Enter your name: ")
   full_pattern(full_name)
   
   
def full_pattern(full_name):
   whitespace_i = full_name.find(" ")
   first_name = full_name[ :whitespace_i]
   last_name = full_name[whitespace_i+1: ]
   pattern(first_name)
   pattern(last_name)
   
def pattern(name):
   name = name.upper()
   for i in range(len(name)):
      print(name[i:])
       
   for j in range(len(name)):
      print(name[ :j+1])
    
main()


dadef if_else_mystery_2(a, b):
    if a * 2 < b:
        a = a * 3
    elif a > b:
        b = b + 3
    if b < a:
        b += 1
    else:
        a -= 1
    print(a, b)
    
    
if_else_mystery_2(10, 2)    