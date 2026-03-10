num=int(input("Enter the number :"))
if(1000<=num<=9999):
   sum=0
   temp=num
   while temp!=0:
      digit=temp%10
      sum+=digit
      temp//=10
   print("sum of digits is :",sum)
else:
   print("Invalid inputs")
