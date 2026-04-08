def rk4(f, t0, y0, h, n):
    """
    Solves the differential equation y' = f(t, y) using the 4th-order Runge-Kutta method.
    """

    # initial conditions
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    # perform n iterations
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values # returns ordered pair(s)