#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:40:43 2019

"""

# problem 1
        
emptyList = []
for x in range(1000):
    if x% 3 == 0 or x % 5 ==0:
        emptyList.append(x)
sum(emptyList)

# problem 2
import sys

emptyList2 = [1, 2]
for x in range(2, sys.maxsize):
    newValue = emptyList2[x-1] + emptyList2[x-2]
    emptyList2.append(newValue)
    if newValue > 4000000:
        break

newList = [x for x in emptyList2 if x % 2 == 0 and x < 4000000]
sum(newList)

# problem 3
