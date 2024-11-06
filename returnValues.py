import math

def main():
   print( displacement(0, 20, 10)) 
    
def displacement(v0, a, t):
   d = v0 * t + 0.5 * a * (t ** 2)
   return d    
    
    
main()
