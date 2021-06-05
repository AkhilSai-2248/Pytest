""" Python Script to find sum of digits of a number """

# Write your code from here

number = input("Enter a number: ")
sum = 0
for i in number :
    sum = sum + int(i)
print("Sum of Digits of a number:",sum)

