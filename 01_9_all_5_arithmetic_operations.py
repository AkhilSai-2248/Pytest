""" Python Script to perform all 5 arthmetic operations +, -, /, *, exponential """

# Write your code from here
u = int(input("enter a number: "))
v = int(input("enter a number: "))

operation = input("enter the operator to be performed(in format -> +,-,*,/,**): ")

if operation == '+' :
    print(u+v)
if operation == '-' :
    print(u-v)
if operation == '*' :
    print(u*v)
if operation == '/' :
    print(u/v)
if operation == '**' :
    print(u**v)
