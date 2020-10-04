#!/usr/bin/python3

print("Calculate Compound Interest \n")

n = int(input("Years (n): "))

p = int(input("Principal (P): "))

i = int(input("Interest in furute, percentage (i): "))

ci = p * (pow((1 + i / 100), n) - 1)

print("Compound interest: {0}".format(round(ci, 2)))
