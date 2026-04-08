def max_error(t_values, y_values, exact_solution):
    """
    Goal: Compute the maximum absolute error over all grid points.

    Function parameters:
        t_values        : list of t values
        y_values        : list of approximate y values
        exact_solution  : function exact_solution(t)

    Returns:
        Maximum absolute error
    """
    errors = [abs(y - exact_solution(t)) for t, y in zip(t_values, y_values)]
    return max(errors)