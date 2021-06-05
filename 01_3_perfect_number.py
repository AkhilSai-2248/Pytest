""" Python Script to check whether a given number is perfect  """

# Write your code from here
inper = int(input("Enter a number: "))
init = 0
for i in range(1, inper) :
    if inper % i == 0 :
        init = init + i

if init == inper :
    print("The given number is a perfect number")
else :
    print("The given number is not a perfect number")