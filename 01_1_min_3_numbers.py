""" Python Script to find minimum among three numbers """

# Write your code from here
j = int(input("Enter a number: "))
k = int(input("Enter a number: "))
l = int(input("Enter a number: "))
if j < k and j < l :
    print(j ," is smaller than ", k,  " and ", l)
if k < j and k < l :
    print(k ," is smaller than ", j,  " and ", l)
if l < j and l < k :
    print(l ," is smaller than ", j,  " and ", k)