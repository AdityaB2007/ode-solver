import math
import matplotlib.pyplot as plt
from ode_solver import euler, heun, rk4

def f(t, y):
    return y

t0 = 0
y0 = 1
h = 0.1
n = 20

t_e, y_e = euler(f, t0, y0, h, n)
t_h, y_h = heun(f, t0, y0, h, n)
t_r, y_r = rk4(f, t0, y0, h, n)

exact_y = [math.exp(t) for t in t_r]

plt.plot(t_e, y_e, label="Euler")
plt.plot(t_h, y_h, label="Heun")
plt.plot(t_r, y_r, label="RK4")
plt.plot(t_r, exact_y, label="Exact")

plt.xlabel("t")
plt.ylabel("y")
plt.title("Numerical Solutions of y' = y")
plt.legend()
plt.show()