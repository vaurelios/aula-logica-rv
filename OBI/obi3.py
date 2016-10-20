#!/bin/env python

comp = input().split(" ")

a, b, c = comp
a = int(a)
b = int(b)
c = int(c)

vals = [a, b, c]
vals.sort()

print(vals[1])

