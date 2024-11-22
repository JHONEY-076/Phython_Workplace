# # import math
# # def main():
# # 
# #    # prompting and rading input data
# #    print("Enter person's information: ")
# #    
# #    height=float(input("height (in cm)?"))
# #    weight=float(input("weight (in kg)?"))
# #    age=float(input("age (in years)?"))
# #    gender=input("gender (male or female)?")
# #    
# #    #calculate the BMR
# #    bmr=10*weight+6.25*height-5*age
# #    if gender=="male":
# #       bmr+=5
# #    else: # female
# #       bmr-=161
# #       
# #    #print the BMR and the classification result   
# #    print("Person's basal metabolic rate =",round(bmr))
# #    
# #    if bmr<1200:
# #       print("low resting burn rate")
# #    elif bmr<=2000:
# #       print("moderate resting burn rate")
# #       
# #    else: 
# #       print("high resting burn rate")
# #       
# # 
# # 
# # main()
# 
# 
# import math
# 
# def calculate_BMI(height,weight):
#      BMI=weight / height**2*703
#      return str(round(BMI,1))
# 
# def classify_BMI(BMI):
#    if float(BMI)<18.5:
#       return "class 1"
#    
#    elif float(BMI)<=24.9:
#       return "class 2"
#       
#    elif float(BMI)<=29.0:
#       return "class 3"
#       
#    else:
#       return "class 4"      
#    
#    
# def main():
#    print("This program reads data for two people")
#    print("and computes their body mass index (BMI).\n")
#    
#    for i in range(1,3):
#       print("Person",str(i), "information:")
#       height=float(input("height (in inches)? "))
#       weight=float(input("weight (in pounds)? "))
#       BMI=calculate_BMI(height,weight)
#       print("BMI =",BMI)    
#       print(classify_BMI(BMI))
#       print()
#       
#    print("Have a nice day!")
# main()      