a=float(input("Enter the mark 1 :"))
b=float(input("Enter the mark 2 :"))
c=float(input("Enter the mark 3 :"))
d=float(input("Enter the mark 4 :"))
e=float(input("Enter the mark 5 :"))
if(a>100 or b>100 or c>100 or d>100 or e>100):
   print("Invalid marks")
else:
   f=(a+b+c+d+e)/5
   print("Average mark :",f)
   if(f>=90):
      print("Grade is O")
   elif(80<=f<=89):
      print("Grade is A+")
   elif(70<=f<=79):
      print("Grade is A")
   elif(60<=f<=69):
      print("Grade is B+")
   elif(55<=f<=59):
      print("Grade is B")
   elif(50<=f<=54):
      print("Grade is C")
   else :
      print("Fail")
