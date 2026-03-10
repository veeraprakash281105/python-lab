p=float(input("Enter principal..."))
n=float(input("Enter nuber of occurence..."))
r=float(input("Enter rate of interest..."))
t=float(input("Enter a time..."))
si=(p*t*r)/100
a=(p*(1+(r/n)/100)**(n*t))
ci=a-p
print("Value of Simple Interest...",si)
print("Value of Compound Interest...",ci)
