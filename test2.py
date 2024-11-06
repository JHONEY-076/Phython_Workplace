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