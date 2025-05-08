
import matplotlib.pyplot as plt

# Parameters
P0 = 100         # Initial population
r = 0.1          # Growth rate
K = 1000         # Carrying capacity
years = 50       # Duration

# FOR loop implementation
pop_for = []
P = P0
for t in range(years + 1):
    pop_for.append(P)
    P = P + r * P * (1 - P / K)

# WHILE loop implementation
pop_while = []
P = P0
t = 0
while t <= years:
    pop_while.append(P)
    P = P + r * P * (1 - P / K)
    t += 1

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(years + 1), pop_for, label='For Loop', marker='o')
plt.plot(range(years + 1), pop_while, label='While Loop', linestyle='--', marker='x')
plt.title("Logistic Population Growth")
plt.xlabel("Years")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
