s1=input("enter the string:")
digit=0
space=0
alphabet=0
for char in s1:
   if char.isdigit():
      digit+=1
   elif char.isspace():
      space+=1
   elif char.isalpha():
      alphabet+=1
print(f"Digits : {digit}")
print(f"Spaces : {space}")
print(f"Alphabets : {alphabet}")
