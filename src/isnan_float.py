#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to determine if a float is NaN in Python?

¿Cómo determinar si un float es NaN en Python?
'''
#
#review IEEE 754 Floating Point Special Values in
#http://legacy.python.org/dev/peps/pep-0754/
#
import math

#create a not a number (NaN)
f = float('nan')
print(f)

#the isnan() method verify if 'f' is a NaN (not a number).
#Return True or False.
print(math.isnan(f))

#create a not a number (NaN)
f1 = 1e309
print(f1)

#Return True because is a division by infinity
print(math.isnan(f1 / f1))
