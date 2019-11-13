next_B = 2  # We start the search at B = 0
gamma = 0.1  # Step size multiplier
precision = 0.00001  # Desired precision of result
max_iters = 1000  # Maximum number of iterations

# Original function
f = lambda B: 3 * B**2 - 5 * B + 4
# Derivative function
df = lambda B: 6 * B - 5

for i in range(max_iters):
    current_B = next_B
    next_B = current_B - gamma * df(current_B)
    step = next_B - current_B
    if abs(step) <= precision:
        break
    print(next_B)

print("Minimum at", next_B)
print("Minimum =", f(next_B))