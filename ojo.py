The Importance of Functions in Programming

Functions are fundamental building blocks in programming that provide several key benefits:

1. Code Reusability: Functions allow you to write code once and reuse it multiple times without rewriting the codes.
2. Modularity: They breakdown complex problems into smaller, manageable parts.
3. Readability: Well-named functions make code more understandable.
4. Maintainability: Changes only need to be made in one place (the function) and it affect all places where the function is used.
5. Abstraction: Functions hide implementation details, exposing only what's needed.
6. Testing: Individual functions can be tested in isolation and helps in fixing bugs.
7. Organization: They help structure code logically.



def nth_root(number, n):
    """Calculate nth root of a number"""
    return number ** (1/n)

def euclidean_distance(point1, point2):
    """Calculate distance between two points (any dimension)"""
    return math.sqrt(sum((a - b)**2 for a, b in zip(point1, point2)))

# Example usage
if __name__ == "__main__":
    print("Nth Root Calculator")
    num = float(input("Enter a number: "))
    root = int(input("Enter root value (e.g., 2 for square root): "))
    print(f"{root}th root of {num} is: {nth_root(num, root):.4f}\n")

    print("Euclidean Distance Calculator")
    print("Enter first point coordinates (comma separated, e.g., 1,2,3)")
    point1 = [float(x) for x in input().split(',')]
    print("Enter second point coordinates (same number of values)")
    point2 = [float(x) for x in input().split(',')]
    print(f"Distance: {euclidean_distance(point1, point2):.4f}")