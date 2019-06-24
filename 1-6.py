# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 01:00:35 2019

@author: user
"""

x = int(input())
y = int(input())
z = int(input())

mi = z /1.6     #一英里 =1.6
y = y + (x * 60)
speed = (mi / y) *60 *60
print ("%.1f" % speed)



