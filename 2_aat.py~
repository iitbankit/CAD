#!/usr/local/bin/python

import sys 
import random 
import operator 

def aat_recursive ( v ) :

  global fanin, MIN, dly


  fanin_of_v = fanin[v]
  
  tmp = MIN
  if ( len(fanin_of_v) > 0 ) :
    for u in fanin_of_v :
      if ( tmp < aat_recursive( u ) + dly[ v ] ) :
        tmp = aat_recursive( u ) + dly[ v ] 
        
    return tmp 
  else :
    return 0

MIN=-999999999  

fanin = [ [], [0], [0], [0,1], [2,3], [1,3,4], [2,3], [1,4,5,6],[],[6,7,8] ]
dly = [1,1,1,1,1,1,1,1,1,1]

print aat_recursive ( 9 )
