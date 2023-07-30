import scipy.optimize
import numpy as np

def f(x, risk_averse, reward_seeking):
    return x[0]**2 + x[1]**2 - risk_averse * x[0] + reward_seeking * x[1]

x0 = np.array([2, 2])

# Define bounds for x and y
bounds = scipy.optimize.Bounds([-10,-10],[10,10])

# Define risk-averse and reward-seeking parameters
risk_averse = 0.5
reward_seeking = 1.0

# Optimize the function with the risk-averse and reward-seeking constraints
result = scipy.optimize.minimize(f, x0, bounds = bounds, args = (risk_averse, reward_seeking))

print(f"The minimum value is: {result.fun}")
print(f"The minimum is located at: {result.x}")
print("Risk-averse:", risk_averse)
print("Reward-seeking:", reward_seeking)