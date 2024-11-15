def main():
   print("Enter person's information")
   height=(int)(input("height (in cm)?"))
   weight=(float)(input("weight (in kg)?"))
   age=int(input("age (in years)?"))
   gender=input("male or female?")
   
   
   
   bmr=10*(weight)+6.25*(height)-5*(age)
   
 bmr = 10 * weight + 6.25 * height - 5 * age
 if sex == "male":
 bmr += 5
 else:
 bmr -= 161
 print("Person's basal metabolic rate = ", round(bmr))
 # print person's resting burn rate
 if bmr < 1200:
 print("low resting burn rate")
 elif bmr <= 2000:
 print("moderate resting burn rate")
 else: # bmr > 2000
 print("high resting burn rate")
   
   
   
main()   