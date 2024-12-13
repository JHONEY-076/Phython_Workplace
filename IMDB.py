def main():
   file=open("imdb.txt")
   lines=file.readlines()
   target=input("Search word?")
   counter=0
   
  
   for line in lines:
        tokens=line.split()
        rank=tokens[0]
        rating= tokens[1]
        votes=tokens[2]
        title=""
        for i in range(3,len(tokens)):
            title+=tokens[i]+" "
        if target.lower()in title.lower():
            if counter==0:
                print("Rank\tVotes\tRating\tTitle")
            print(f"{rank}\t\t{votes}\t{rating}\t\t{title}")        
            counter+=1
           
   print(f"{counter} matches.")   
            
        
        
        
main()      
   