# for ee-677-2016 ( preparing and solving LP for 1-d placement ( without timing )
# needs python-cvxopt ( prompt> sudo apt-get install python-cvxopt )
# also needs numpy ( part of scipy or separate )
# Sachin B. Patkar ( 13th Aug 2016 )

#     minimize summation Lji over all i,j such that j->i
# subject to
#       0 <= x(i) <= WIDTH  for all i
#       x(p) = X(p) for p among fixedCells
#       Lji >= x(j) - x(j)  for j->i
#       Lji >= x(i) - x(i)  for j->i
#       Lji >= minimum_separation  for j->i


from cvxopt import matrix, solvers
import numpy
import random

def createLP_cvxopt_sys ( fanin , fixedCells, fixedLocations, WIDTH ) :

  V = range( len(fanin) ) 
  A_list = [ ]
  b_list = [ ]

  num_lji_vars = 0
  for k in fanin :
    num_lji_vars += len( k )

  index_of_lji_var = len(V)
  cost_list = [ 0.0 for i in range( len(V) + num_lji_vars ) ]
  for i in range( len(V) , len(V) + num_lji_vars ) :
    cost_list[ i ] = 1.0 
  print "printing cost_list" , cost_list

  for v in V :
    tmp_row = [ 0.0 for i in range( len(V) + num_lji_vars ) ]
    tmp_row[ v ] = -1.0
    b_list.append ( 0.0 )
    A_list.append ( tmp_row )
    print "adding constraint ", tmp_row[v], "x[", v, "]  <= ", "0"

    tmp_row = [ 0.0 for i in range(len(V) + num_lji_vars) ]
    tmp_row[ v ] = 1.0
    b_list.append ( WIDTH )
    A_list.append ( tmp_row )
    print "adding constraint ", tmp_row[v], "x[", v, "]  <= ", WIDTH

  for k in range(len(fixedCells)) :
    tmp_row = [ 0.0 for i in range(len(V) + num_lji_vars) ]
    tmp_row[ fixedCells[k] ] = -1.0
    b_list.append ( -1.0 * fixedLocations[k] )
    A_list.append ( tmp_row )
    print "adding constraint ", tmp_row[fixedCells[k]], "x[", fixedCells[k], "]  <= ", -1.0 * fixedLocations[k]

    tmp_row = [ 0.0 for i in range(len(V) + num_lji_vars) ]
    tmp_row[ fixedCells[k] ] = +1.0
    b_list.append ( 1.0 * fixedLocations[k] )
    A_list.append ( tmp_row )
    print "adding constraint ", tmp_row[fixedCells[k]], "x[", fixedCells[k], "]  <= ", 1.0 * fixedLocations[k]
    
  index_of_lji_var = len(V)
  for ii  in V :
    for jj in fanin[ ii ] : 
      tmp_row = [ 0.0 for i in range(len(V) + num_lji_vars) ]
      tmp_row[ index_of_lji_var ] = -1.0
      tmp_row[ ii ] = 1.0
      tmp_row[ jj ] = -1.0
      b_list.append ( 0.0 )
      A_list.append ( tmp_row )
      print "adding constraint ", tmp_row[jj], "x[", jj, "] +", tmp_row[ii], " x[",ii,"] + ",tmp_row[index_of_lji_var]," lji[",jj,ii,"] <= ", "0"

      tmp_row = [ 0.0 for i in range(len(V) + num_lji_vars) ]
      tmp_row[ index_of_lji_var ] = -1.0
      tmp_row[ ii ] = -1.0
      tmp_row[ jj ] = 1.0
      b_list.append ( 0.0 )
      A_list.append ( tmp_row )
      print "adding constraint ", tmp_row[jj], "x[", jj, "] +", tmp_row[ii], " x[",ii,"] + ",tmp_row[index_of_lji_var]," lji[",jj,ii,"] <= ", "0"
 
      index_of_lji_var = index_of_lji_var + 1

  index_of_lji_var = len(V)
  for ii  in V :
    for jj in fanin[ ii ] : 
      tmp_row = [ 0.0 for i in range(len(V) + num_lji_vars) ]
      tmp_row[ index_of_lji_var ] = -1.0
      b_list.append ( -100.0 )
      A_list.append ( tmp_row )
      print "adding constraint ", tmp_row[index_of_lji_var], "lji[", ii,jj, "]  <= ", "-100.0"
    
      index_of_lji_var = index_of_lji_var + 1

  return A_list, b_list, cost_list
       
      
def preparefanin_from_fanout ( fanout ) :
  fanin = [ [] for i in range( len( fanout ) ) ] 
  for i in range( len( fanout ) ) :
    for j in range( len(fanout[i]) ) :
      fanin[ fanout[i][j] ].append(i)  
  return fanin

fanout = [ [ 1, 2, 3 ], [ 3, 5, 7 ], [4, 6], [4, 5, 6], [5, 7], [7], [7,9], [9], [9], [] ]
fanin = preparefanin_from_fanout( fanout )
  
fixedCells = [0,4,6,8,9]
fixedLocations = [0, 400, 600, 800,  900 ]
WIDTH = 1000
A_l, b_l, c_l = createLP_cvxopt_sys ( fanin , fixedCells, fixedLocations, WIDTH ) 

A_matrix = matrix( numpy.array(A_l).transpose().tolist() )
b_matrix = matrix ( b_l )
c_matrix = matrix ( c_l )

print "DIM are ", A_matrix.size, len(b_matrix), len(c_matrix)

sol=solvers.lp(c_matrix,A_matrix,b_matrix, solver='glpk')
print ( sol['x'] )

print "optimum placement along X-axis is ", [ sol['x'][i] for i in range(len(fanin)) ]

