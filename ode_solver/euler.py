def euler(f, t0, y0, h, n):
    """
    Solves the differential equation y' = f(t, y) using Euler's method.

    function parameters:
        f  : function of the form f(t, y)
        t0 : initial time
        y0 : initial value
        h  : step size
        n  : number of steps

    returns the ordered pair(s):
        (t_values, y_values)
    """

    # initial conditions
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    # perform n iterations
    for _ in range(n):
        y = y + h * f(t, y) # Euler's method
        t = t + h # step size = h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values # returns ordered pair(s)