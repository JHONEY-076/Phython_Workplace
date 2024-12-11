def show_twos(n):
    original = n
    factors = ""

    while n % 2 == 0:
        factors += "2 * "
        n //= 2

    factors += str(n)
    print(f"{original} = {factors}")

show_twos(7)
show_twos(18)
show_twos(-68)
show_twos(120)
show_twos(-32)

