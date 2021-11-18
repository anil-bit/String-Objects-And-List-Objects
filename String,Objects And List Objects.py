#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:42:03 2021

@author: anil
"""



'''
1. Create the below pattern using nested for loop in Python.
'''
d = "*";s = 1;e = 5;j = 1
for ll in range(2):
    for o in range(s,e,j):
        print(d*o)
        s = 5;e = -1;j = -1
        
'''
2. Write a Python program to reverse a word after accepting the input from the user.    
'''   
word = input("enter the word:")
print(word[::-1])