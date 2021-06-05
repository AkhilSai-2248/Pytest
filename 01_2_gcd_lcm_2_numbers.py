""" Pqthon Script to find GCD and LCM of 2 numbers """

# Write qour code from here
import math
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))

gcd = math.gcd(p, q)
lcm = (p * q)/gcd

print("Gcd and Lcm of ", p, ",", q, " are ", gcd, ",", lcm, " respectivelq")