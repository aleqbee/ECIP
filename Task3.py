import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Task 1: True system
# x(t+1) = x(t) + 1
# -----------------------------
N = 50
x0 = 0

t = np.arange(N + 1)
x_true = np.zeros(N + 1, dtype=float)
x_true[0] = x0
for k in range(N):
    x_true[k + 1] = x_true[k] + 1

# -----------------------------
# Task 2: Noisy observations
# y(t) = x(t) + noise, noise ~ N(0, 2)
# -----------------------------
noise_mean = 0.0
noise_std = 2.0
noise = np.random.normal(noise_mean, noise_std, size=N + 1)
y = x_true + noise

# -----------------------------
# Task 3: Moving average estimator
# x_hat(t) = average of last W observations
# -----------------------------
W = 5  # window size (try 3, 5, 10)

x_hat = np.zeros_like(y)
for i in range(len(y)):
    start = max(0, i - W + 1)      # beginning of window
    x_hat[i] = np.mean(y[start:i+1])

# -----------------------------
# Plot: true, noisy, estimated
# -----------------------------
plt.figure()
plt.plot(t, x_true, label="True state x(t)", linewidth=2)
plt.scatter(t, y, label="Noisy obs y(t)", alpha=0.6)
plt.plot(t, x_hat, label=f"Estimated state x̂(t) (MA, W={W})", linewidth=2)

plt.xlabel("t (time step)")
plt.ylabel("Value")
plt.title("True vs Noisy vs Moving Average Estimate")
plt.grid(True)
plt.legend()
plt.show()