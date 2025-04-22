


def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method for finding roots of f(x) = 0
    Parameters:
        f       : Function whose root is to be found
        df      : Derivative of the function
        x0      : Initial guess
        tol     : Tolerance for stopping
        max_iter: Maximum number of iterations
    Returns:
        Approximate root
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero. No solution found.")
        dx = fx / dfx
        x = x - dx
        if abs(dx) < tol:
            return x
    raise RuntimeError("Maximum iterations exceeded")

# Example 1: Solve x^2 - 2 = 0 (Root is sqrt(2))
def f1(x): return x**2 - 2
def df1(x): return 2*x

root1 = newton_raphson(f1, df1, x0=1.0)
print("Root of x^2 - 2 = 0:", root1)

# Example 2: Solve x^3 - x - 1 = 0 (real root near 1.32)
def f2(x): return x**3 - x - 1
def df2(x): return 3*x**2 - 1

root2 = newton_raphson(f2, df2, x0=1.5)
print("Root of x^3 - x - 1 = 0:", root2)