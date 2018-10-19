# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:26:55 2018

@author: mizuk
"""

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"
        
    def say_hello(self):
        print(self.msg + " " + self.target)
        
class Hello(Greeting):
    def say_hello(self, target):
        print(self.msg + " " + target)
        
player = Hello()
player.say_hello("python")