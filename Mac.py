

def compare_root_finding_methods(f, f_prime, a, b, x0, tol=1e-6, max_iter=100):
    """
    Compares Bisection and Newton-Raphson methods for finding roots.

    Parameters:
        f        : function for which root is to be found
        f_prime  : derivative of the function (required for Newton-Raphson)
        a, b     : interval for bisection (must bracket a root)
        x0       : initial guess for Newton-Raphson
        tol      : tolerance for stopping criterion
        max_iter : maximum number of iterations for both methods

    Returns:
        Dictionary with step counts and root approximations for both methods
    """
    # Bisection Method
    def bisection(f, a, b, tol, max_iter):
        if f(a) * f(b) >= 0:
            raise ValueError("f(a) and f(b) must have opposite signs")

        steps = 0
        while (b - a) / 2.0 > tol and steps < max_iter:
            c = (a + b) / 2.0
            if f(c) == 0:
                break
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            steps += 1
        return (steps, (a + b) / 2.0)

    # Newton-Raphson Method
    def newton_raphson(f, f_prime, x0, tol, max_iter):
        steps = 0
        x = x0
        for _ in range(max_iter):
            fx = f(x)
            fpx = f_prime(x)
            if fpx == 0:
                raise ZeroDivisionError("Derivative is zero at x = {}".format(x))
            x_new = x - fx / fpx
            steps += 1
            if abs(x_new - x) < tol:
                break
            x = x_new
        return (steps, x)

    bisection_result = bisection(f, a, b, tol, max_iter)
    newton_result = newton_raphson(f, f_prime, x0, tol, max_iter)

    return {
        "bisection": {"steps": bisection_result[0], "root": bisection_result[1]},
        "newton_raphson": {"steps": newton_result[0], "root": newton_result[1]}
    }
