def print_solution_table(name, t_values, y_values, exact_solution=None):
    print(f"\n{name}")
    print("-" * 60)

    if exact_solution is None:
        print(f"{'t':<10}{'Approx y':<20}")
        for t, y in zip(t_values, y_values):
            print(f"{t:<10.4f}{y:<20.8f}")
    else:
        print(f"{'t':<10}{'Approx y':<20}{'Exact y':<20}{'Abs Error':<20}")
        for t, y in zip(t_values, y_values):
            exact = exact_solution(t)
            error = abs(y - exact)
            print(f"{t:<10.4f}{y:<20.8f}{exact:<20.8f}{error:<20.8f}")