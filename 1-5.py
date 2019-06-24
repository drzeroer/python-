# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 00:34:01 2019

@author: user
"""
"""
輸入高、寬 求周長、面積
輸出需顯示小數點後兩位
"""

a = float(input())
b = float(input())

hight = float (a)
width = float (b)
perimeter = (a * 2) + (b * 2)           #周長
Area = (a * b)                          #面積


print ("%.2f" % hight)
print ("%.2f" % width)
print ("%.2f" % perimeter)
print ("%.2f" % Area)
