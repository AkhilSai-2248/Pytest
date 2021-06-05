""" Python Script to find primes numbers upto a specified limit """

# Write your code from here
pl=int(input("Enter the limit of primes: "))
primes_list = []
for i in range (2, pl+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        primes_list.append(i)
        
print(primes_list)

