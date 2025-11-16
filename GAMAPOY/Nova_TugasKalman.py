# Section 1: Understanding the principles of Kalman Filters

import numpy as np
import matplotlib.pyplot as plt
# Generate data for simulation
np.random.seed(0)
n = 50
x = np.linspace(0, 10, n)
y = 2*x + 1 + np.random.normal(0, 1, n)
# Kalman Filter implementation
def kalman_filter(data, Q=1, R=5):
    n = len(data)
    x_hat = np.zeros(n)    # Predicted state estimate
    P = np.zeros(n)        # Predicted error covariance
    x_hat_minus = np.zeros(n)
    P_minus = np.zeros(n)
    for k in range(1, n):
        # Time update
        x_hat_minus[k] = x_hat[k-1]
        P_minus[k] = P[k-1] + Q
        # Measurement update
        K = P_minus[k] / (P_minus[k] + R)
        x_hat[k] = x_hat_minus[k] + K * (data[k] - x_hat_minus[k])
        P[k] = (1 - K) * P_minus[k]
    return x_hat
# Applying Kalman Filter to the generated data
filtered_data = kalman_filter(y)
# Plotting the original data and filtered data
plt.figure(figsize=(12, 6))
plt.plot(x, y, label='Original Data', marker='o')
plt.plot(x, filtered_data, label='Filtered Data', marker='x')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Kalman Filter Applied to Time Series Data')
plt.show()