def calculate_bmi(h,w):
   return w/h**2*703;

def classify_class(BMI):
   
    if BMI < 18.5:
        return "class 1"
    elif BMI <= 24.9:
        return "class 2"
    elif BMI <= 29.9:
        return "class 3"
    else:
        return "class 4"


def main():
   print("This program reads data for two people\nand computes their body mass index (BMI).");
   print();
   
   for i in range(1,3):
      print("Person "+str(i)+" information:");
      h=float(input("height (in inches)? "));
      w=float(input("weight (in pounds)? "));
      
      BMI=calculate_bmi(h,w)
      print("BMI = "+str(round(BMI,1)))
      bmi_class=classify_class(BMI)
      print(bmi_class);
      print()   
   
   print("Have a nice day!");
   
   
main()