import numpy as np
import matplotlib.pyplot as plt

# Task 1 — Simulate the True System State
# System: x(t+1) = x(t) + 1

N = 50          # number of time steps
x0 = 0          # initial state (choose any value you want)

t = np.arange(N + 1)          # time index: 0..50 (51 points)
x = np.zeros(N + 1, dtype=float)
x[0] = x0

for k in range(N):
    x[k + 1] = x[k] + 1

# Plot the evolution of the true state
plt.figure()
plt.plot(t, x, marker='o')
plt.xlabel("t (time step)")
plt.ylabel("x(t) (true state)")
plt.title("True System State: x(t+1) = x(t) + 1")
plt.grid(True)
plt.show()