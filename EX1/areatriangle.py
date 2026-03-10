import math
a=int(input("enter 1 for base and height or 2 for sides:"))
if(a==1):
   b=int(input("enter the base value:"))
   c=int(input("enter the height value:"))
   if(b<=0 or c<=0):
      print("invalid value")
   else:
      area=(b*c)/(2)
      print("area of triangle:",area)
elif(a==2):
   d=int(input("enter side a"))
   e=int(input("enter side b"))
   f=int(input("enter side c"))
   if(d<=0 or e<=0 or f<=0):
      print("invalid value")
   else:
      s=(d+e+f)/(2)
      area1=math.sqrt(s*(s-d)*(s-e)*(s-f))
      print("area if triangle",area1)
else:
   print("enter valid choice 1 or 2")
