import matplotlib.pyplot as plt
from ode_solver import euler, heun, rk4

# logistic growth equation
def f(t, y):
    return y * (1 - y)

t0 = 0.0
y0 = 0.1
h = 0.1
n = 100

t_e, y_e = euler(f, t0, y0, h, n)
t_h, y_h = heun(f, t0, y0, h, n)
t_r, y_r = rk4(f, t0, y0, h, n)

plt.plot(t_e, y_e, label="Euler")
plt.plot(t_h, y_h, label="Heun")
plt.plot(t_r, y_r, label="RK4")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Logistic Growth ODE")
plt.legend()
plt.show()