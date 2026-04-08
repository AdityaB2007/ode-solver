import math
from ode_solver import euler, heun, rk4, max_error

def f(t, y):
    return y

def exact(t):
    return math.exp(t)

def test_solver_accuracy_order():
    t0 = 0.0
    y0 = 1.0
    h = 0.1
    n = 10

    t_e, y_e = euler(f, t0, y0, h, n)
    t_h, y_h = heun(f, t0, y0, h, n)
    t_r, y_r = rk4(f, t0, y0, h, n)

    err_e = max_error(t_e, y_e, exact)
    err_h = max_error(t_h, y_h, exact)
    err_r = max_error(t_r, y_r, exact)

    assert err_h < err_e
    assert err_r < err_h