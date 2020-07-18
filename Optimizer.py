# Importing linprog (linear programming) from scipy(scientific python)
from scipy.optimize import linprog

#  Let Decision variables x and y
#  Constraints 100x+200y <= 10000 , 10x+30y <= 1200 , x+y<=110
#  The limits or boundaries for decision variables x >=0 and y>=0


# defining objective function from problem 50x + 120y --> MAX
obj_func=[-50,-120]

# Taking LHS of the constraints
lhs_inequality = [[100,200],[10,30],[1,1]]

# Taking RHS of the constraints
rhs_inequality = [[10000,1200,110]]

# Giving the limits or boundaries to decision variables (x >= 0 and y >=0 )
boundaries = [(0,float('inf')),(0,float('inf'))]

optimiation = linprog(c = obj_func, A_ub =lhs_inequality, b_ub=rhs_inequality,bounds=boundaries,method='Simplex')

optimiation # NOTE : after execution last line x: array([a,b]) where a and b are the only answers needed
