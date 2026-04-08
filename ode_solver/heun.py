def heun(f, t0, y0, h, n):
    """
    Solves the differential equation y' = f(t, y) 
    using Heun's method (Improved Euler).
    """

    # initial conditions
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    # perform n iterations
    for _ in range(n):
        slope1 = f(t, y)
        predictor = y + h * slope1
        slope2 = f(t + h, predictor)

        y = y + (h / 2) * (slope1 + slope2) # Heun's method
        t = t + h # step size = h

        # increase the number of solution pairs
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values # returns ordered pair(s)