def show_twos(n):
    negative = False 
    if n < 0:
        negative = True
        n = abs(n)

    print(f"{'-' if negative else ''}{n} = ", end="")

    first = True
    
    # First handle the factorization of 2
    while n % 2 == 0:
        if first:
            print("2", end="")
            first = False
        else:
            print(" * 2", end="")
        n //= 2
    
    # Now handle the remaining part of the number
    if n > 1:
        if not first:
            print(f" * {n}", end="")  
        else:
            print(n, end="")  
    else:
        print(end="")  

    # If the number was negative, print the negative factor at the end
    if negative and n > 1:
        print(f" *", end="")  
    elif negative and n == 1:
        print(f" * ", end="")  
    
    print() 


# Test cases
show_twos(7)    # 7 = 7
show_twos(18)   # 18 = 2 * 3 * 3
show_twos(-68)  # -68 = 2 * 2 * 17 * -1
show_twos(120)  # 120 = 2 * 2 * 2 * 3 * 5
show_twos(-10)  # -10 = 2 * -5
