

import matplotlib.pyplot as plt

# Generate data
x = list(range(1, 1001))
y = [i**2 for i in x]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='y = x²', color='blue')
plt.title('Squares of Numbers from 1 to 1000')
plt.xlabel('Number (x)')
plt.ylabel('Square (x²)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
