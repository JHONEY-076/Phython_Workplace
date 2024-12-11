
def average_value_in_file(name):
   
   file=open(name)
   lines=file.read().split()
   total = 0
   counter = 0
   for i in range(len(lines)):
      total += float(lines[i])
      counter += 1
   
   return total / counter

print(average_value_in_file("input.txt"))
 
