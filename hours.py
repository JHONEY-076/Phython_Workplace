f= open("hours.txt")
lines=f.readlines()
for line in lines:
   tokens=line.split()
   id=tokens[0]
   name=tokens[1]
   sum_hours=0
   days_counter=0
   
   for i in range(2,len(tokens)):
      sum_hours=float(token[i])
      days_counter+=1   
   avg_hours=sum_hours/days_counter  
   print(f"{name} (ID{id})",end="" )
   print(f"worked {round(sum_hours,1)} hours",end="")
   print(f"({round(avg_hours,2)}hours/day)") 
   
 