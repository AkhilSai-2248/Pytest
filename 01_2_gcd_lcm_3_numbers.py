""" Python Script to find GCD and LCM of 3 numbers """

# Write your code from here
import math

s = int(input("Enter first number: "))
t = int(input("Enter second number: "))
u = int(input("Enter third number: "))

gcd_stu = math.gcd(math.gcd(s, t), u)
gcd_st = math.gcd(s, t)
gcd_su = math.gcd(s, u)
gcd_tu = math.gcd(t, u)

lcm_stu = int((s*t*u*gcd_stu)/(gcd_st*gcd_tu*gcd_su))

print("gcd and lcm of ",s, ",", t, ",", u, " are ", gcd_stu, ",", lcm_stu, "respectively")

