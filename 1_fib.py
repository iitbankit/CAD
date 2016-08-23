#!/usr/local/bin/python

import sys 
import random 
import operator 

def fib(n) :
      global b 
      if n == 1 or n == 2 :
         return 1  
      else :
         return fib(n-1) + fib(n-2) 
b = 0 
print fib(4)
