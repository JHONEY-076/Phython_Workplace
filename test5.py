# text=input("Your message? ")
# key=int(input("Encoding key? "))
# text=text.upper()
# 
# for letter in text:
#    if letter>= "A" and letter<="Z": 
#       shifted_num=ord(letter)+key
#       if shifted_num>ord("Z"):
#          shifted_num=shifted_num%ord('[')+ord('A')
#       elif shifted_num<ord("A"):
#          shifted_num=ord('Z') - ord('@')%shifted_num      
#       print(chr(shifted_num),end="")
#       
#    else:
#       print(letter, end="")
# 
#    

# 
# def main():
#    add_commas("12345678")
#    
# 
# 
# 
# def add_commas(num):
#    
#        
#       


# 
# def main():
# 
#   print(reverse("Pikachu"))
# 
# 
# def reverse(name):
#    
#    result=""
#    for i in range(len(name)-1,-1,-1):
#        result+=name[i]
#    return result      
#    
# 
# 
# main()
# 
# 
# def main():
#     reversed_name = reverse("Pikachu")
#     print(reversed_name)
# 
# def reverse(name):
#     return name[::-1]
# 
# main()



# def is_prime_number(num):
#     if num <= 1:
#         return False  
#     if num == 2:
#         return True  
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# 
# print(is_prime_number(80)) 
# print(is_prime_number(79))  
# print(is_prime_number(2))   
# 
# 
# 

# 
# def factor_count(num):
#    
#    count=0
#    
#    for i in range(1,num+1):
#       if num%i==0:
#          count+=1
#    return count   
#    
# print(factor_count(24))
# 


def add_commas(number_str):
   
    length = len(number_str)
    
   
    result = ''
    
    for i in range(length):
        
        result = number_str[length - 1 - i] + result
        
        
        if (i + 1) % 3 == 0 and i != length - 1:
            result = ',' + result
    
    return result

print(add_commas("12345678"))