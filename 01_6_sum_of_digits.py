""" Python Script to find sum of digits of a number """

# Write your code from here

num = input("Enter a number: ")
sum = 0
for i in num :
    sum = sum + int(i)
print("Sum of Digits of a number:",sum)
