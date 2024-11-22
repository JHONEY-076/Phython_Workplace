# def print_letters(word):
#    #post(letter)
#    print(word[0],end="")
#    for i in range(1,len(word)):
#       print(",",end="")
#       print(word[i],"")
#    print()   
#       


def print_letters(word):
  
  
   for i in range(len(word)-1):
       print(word[i],end="")
       print(",",end="")
   
      length=len(word)-1
    print(word[length])
  
   print(word[-1])
   print()   
     



      
print_letters("example")

# def main():
#    print_primes(7)
# 
# 
# 
# 
# def print_primes(max):
#    for i in range(2,max+1):
#       if is_prime(i):
#          if(is_first):
#             print(i,end="")
#             is_first=False
#          else:   
#             print(",", str(i),end="")
#    print()         
#             
# 
# 
# def is_prime(num):
#    return count_factors(num)==2
# 
# def count_factors(num):
#    factors=0
#    for i in range(1, num+1):
#       if(num%i==0):
#          factors+=1
#    return factors
#          
# main()     