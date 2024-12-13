f=open("gasprices.txt")
contents=f.read()
tokens =contents.split()

sum_price_bel=0
sum_price_usa=0
counter=0

for i in range(0,len(tokens),3):
   sum_price_bel+=float(tokens[i])
   sum_price_usa+=float(tokens[i+1])
   counter+=1
   
avg_price_bel=sum_price_bel/counter
avg_price_usa=sum_price_usa/counter
   
     
     
        
print("Belgium average:", avg_price_bel)         
        
print("USA average:", avg_price_usa)         
   
      
   
