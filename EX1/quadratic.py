import math
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
x=(-b)/(2*a)
y=(b**2)-(4*a*c)
if(y>0):
    d=(-b+math.sqrt(y))/(2*a)
    e=(-b-math.sqrt(y))/(2*a)
    print("The roots are real and distinct:")
    print("Root1:{0} Root2:{1}".format(d,e))
elif(y<0):
    f=(math.sqrt(-y))/(2*a)
    print("the roots are real and imaginary:")
    print("Root1:{0}+{1}j".format(x,f))
    print("Root1:{0}-{1}j".format(x,f))
else:
    g=(-b+math.sqrt(y))/(2*a)
    print("the roots are real and equal:")
    print("Root1:{0}".format(g))
