def check(String):
   up = 0
   low = 0
   for char in String:
      if char.isupper():
         up += 1
      elif char.islower():
         low += 1
   print(f"Upper: {up}")
   print(f"Lower: {low}")
sentence = input("Enter the string: ")
check(sentence)
