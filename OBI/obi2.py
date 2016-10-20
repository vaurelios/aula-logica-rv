#!/bin/env python

from math import sqrt

num = int(input())
quads = 0

sobrando = num
while sobrando != 0:
    lado = int(sqrt(sobrando))
    sobrando = sobrando - (lado * lado)
    quads += 1

print(quads)
