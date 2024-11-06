def print_design():

   for i in range(1, 10, 2):
    spaces = (11 - i) // 2 
    print('-' * spaces + str(i) * i + '-' * spaces)



print_design()


