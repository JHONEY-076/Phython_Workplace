import math
def main():

   # prompting and rading input data
   print("Enter person's information: ")
   
   height=float(input("height (in cm)?"))
   weight=float(input("weight (in kg)?"))
   age=float(input("age (in years)?"))
   gender=input("gender (male or female)?")
   
   #calculate the BMR
   bmr=10*weight+6.25*height-5*age
   if gender=="male":
      bmr+=5
   else: # female
      bmr-=161
      
   #print the BMR and the classification result   
   print("Person's basal metabolic rate =",round(bmr))
   
   if bmr<1200:
      print("low resting burn rate")
   elif bmr<=2000:
      print("moderate resting burn rate")
      
   else: 
      print("high resting burn rate")
      


main()