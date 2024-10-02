HEIGHT=8
WIDTH=16
 
 def main():
    draw_box()
 
 def draw_box():
    
    top_bottom_line()
    for i in range(HEIGHT):
       middle_line()
    top_bottom_line()
    
 
 def middle_line():
    print("|",end="")
    print(WIDTH* " ",end="")
    print("|")
    
 
 def top_bottom_line():
    print("+", end="")
    print(WIDTH*"/\\",end="")
    print("+")
    
    
 main()   

# def ascii_figure():
#     height = 5
# 
#     for i in range(height):
#       num_slashes = height - i - 1       
#                
#       num_asterisks = i * 8     
# 
#       line = ('////' * num_slashes) + ('*' * num_asterisks) + ('\\\\\\\\' * num_slashes)
#         
#       print(line)
# 
# ascii_figure()
# 