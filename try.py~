from cvxopt import matrix, solvers
import numpy
import random

def fanin1(fanout) :
  fanin = [ [] for i in range( len( fanout ) ) ] 
  for i in range( len( fanout ) ) :
    for j in range( len(fanout[i]) ) :
      fanin[ fanout[i][j] ].append(i)  
  return fanin

fanout = [ [ 1, 2, 3 ], [ 3, 5, 7 ], [4, 6], [4, 5, 6], [5, 7], [7], [7,9], [9], [9], [] ]
fanin = fanin1(fanout)
  
fcel = [0,4,6,8,9]
floc = [0, 400, 600, 800,  900 ]
 
alist = []
blist = []

hun = -100
width = 1000
zero = 0.0
one = 1.0
neg = -1.0
no_fanin = len(fanin)
temp = 0 

#print fanin
lenfc = len(fcel)

# temp = total connections 

for x in range (0,no_fanin):
    temp = temp + len(fanin[x])  
for x in range (0,no_fanin) :
    templ = [0.0 for i in range(0,no_fanin+temp)]
    templ[x] = neg  
    alist.append(templ)
    blist.append(zero)
    templ[x] = one
    alist.append(templ)
    blist.append(width)  
    for y in range (0,lenfc):
        if x == fcel[y] :
            blist.pop()
            blist.pop()
            blist.append(floc[y])
            blist.append(floc[y])
    #print blist

# alist = list of coff 
# blist = list of constants 

# lij constaint 
k = lenfc
for i in range (0,no_fanin) :
    for j in fanin[i] :
        templ = [0.0 for i in range(0,no_fanin+temp)]
        templ[i] = one
        templ[j] = neg
        templ[k] = neg 
        blist.append(zero)
        alist.append(templ)
        templ[i] = neg
        templ[j] = one
        templ[k] = neg 
        blist.append(zero)
        alist.append(templ)

# minimum separation 

for i in range (0,no_fanin) :
    for j in fanin[i] :
        templ = [0.0 for i in range(0,no_fanin+temp)]
        templ[k] = neg
        alist.append(templ)
        blist.append(hun) 


A_matrix = matrix( numpy.array(alist).transpose().tolist() )
b_matrix = matrix (blist)

print A_matrix , b_matrix 























