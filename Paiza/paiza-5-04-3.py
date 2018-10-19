# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:49:10 2018

@author: mizuk
"""

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0

for key in points:
    sum +=points[key]
print(int(sum))