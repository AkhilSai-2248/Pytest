""" Python Script to find twin primes upto a specified limit """

# Write your code from here
prlt=int(input("Enter the limit of primes: "))
prlst = []
for h in range (2, prlt+1):
    for q in range(2, h):
        if h%q == 0:
            break
    else:
        prlst.append(h)
prlt = len(prlst)
twnprlst = []
for h in range(0, prlt-1) :
    if (prlst[h+1] - prlst[h] == 2):
        twnprlst.append(prlst[h:h+2])
print(twnprlst)