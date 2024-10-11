def main():
   line(13)
   
   line(7)
   
   line(35)
   
   
    # w h
   box(10,3)
   box(5,4)
   
   
   
def line(num):
   print("*"*num)   


def box(w, h):
    print("*"*w)
    for i in range(h):
      print("*", end="")   
      print(" "*(w-2), end="")
      print("*")
    
    print("*"*w)




main()