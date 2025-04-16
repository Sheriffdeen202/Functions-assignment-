Recursion is a programming concept where a function calls itself to solve a smaller instance of the same problem, continuing until it reaches a base case. This is often used for tasks that can be broken down into similar subtasks like tree traversal, backtracking problems, or divide-and-conquer algorithms.

def arithmetic_progression(a, d, n):
    print("Arithmetic Progression:")
    for i in range(n):
        term = a + i * d
        print(term, end=' ')
    print()
    total = (n / 2) * (2 * a + (n - 1) * d)
    print(f"Sum of AP: {total}")
    
    def geometric_progression(a, r, n):
    print("Geometric Progression:")
    for i in range(n):
        term = a * r**i
        print(term, end=' ')
    print()
    if r != 1:
        total = a * (r**n - 1) / (r - 1)
    else:
        total = a * n
    print(f"Sum of GP: {total}")