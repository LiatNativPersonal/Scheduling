# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:07:15 2020

@author: liatn
"""
import random

class inputsGenerator:
    
    def __init__(self, N, lower_bound, upper_bound, filename):
        self.N = N
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.filename = filename
    
    def generateInputs(self):
        with open(self.filename, 'w+')as output:
            for i in range(self.N):
                value = random.randrange(self.lower_bound, self.upper_bound)
                output.write("1,{},{}\n".format(i,value))
            for i in range(2*self.N):
                value = random.randrange(self.lower_bound, self.upper_bound)
                output.write("1,{},{}\n".format(i,value))
        