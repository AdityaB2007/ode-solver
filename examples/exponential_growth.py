import math
from ode_solver import euler, heun, rk4, max_error
from ode_solver.utils import print_solution_table

def f(t, y):
    return y

# exponential growth equation
def exact(t):
    return math.exp(t)

t0 = 0.0
y0 = 1.0
h = 0.1
n = 10

t_e, y_e = euler(f, t0, y0, h, n)
t_h, y_h = heun(f, t0, y0, h, n)
t_r, y_r = rk4(f, t0, y0, h, n)

print_solution_table("Euler Method", t_e, y_e, exact)
print_solution_table("Heun Method", t_h, y_h, exact)
print_solution_table("RK4 Method", t_r, y_r, exact)

print("\nMaximum Errors")
print("-" * 60)
print("Euler:", max_error(t_e, y_e, exact))
print("Heun :", max_error(t_h, y_h, exact))
print("RK4  :", max_error(t_r, y_r, exact))