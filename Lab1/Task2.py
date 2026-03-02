import numpy as np
import matplotlib.pyplot as plt

# ---------- Task 1: True System ----------
# x(t+1) = x(t) + 1

N = 50
x0 = 0

t = np.arange(N + 1)
x_true = np.zeros(N + 1)
x_true[0] = x0

for k in range(N):
    x_true[k + 1] = x_true[k] + 1


# ---------- Task 2: Noisy Observations ----------
# y(t) = x(t) + noise
# noise ~ N(0, 2)

noise_mean = 0
noise_std = 2

noise = np.random.normal(noise_mean, noise_std, N + 1)
y = x_true + noise


# ---------- Plot ----------
plt.figure()
plt.plot(t, x_true, label="True state x(t)", linewidth=2)
plt.scatter(t, y, label="Noisy observations y(t)", alpha=0.7)

plt.xlabel("t (time step)")
plt.ylabel("State value")
plt.title("True State vs Noisy Observations")
plt.legend()
plt.grid(True)
plt.show()
