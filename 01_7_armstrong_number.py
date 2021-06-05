""" Python Script to find whether a number is armstrong or not """

#Write your code from here
Value = input("Enter a number: ")
init = 0
l = int(Value)
while l > 0:
   unit = l % 10
   init = init + (unit ** len(Value))
   l = l // 10
if int(Value) == init:
   print(Value,"is an Armstrong Valueber")
else:
   print(Value,"is not an Armstrong number")
