import scipy.optimize
import matplotlib.pyplot as plt
import numpy as np

def f(x, risk_averse, reward_seeking):
    return x[0]**2 + x[1]**2 - risk_averse * x[0] + reward_seeking * x[1]

# Define the scenarios
scenarios = [
    [0.1, 0.2],
    [0.2, 0.4],
    [0.3, 0.6],
    [0.4, 0.8],
    [0.5, 1.0]
]

# Define the bounds for x and y
bounds = scipy.optimize.Bounds([0, 0], [1, 1])

# Generate the bar chart
fig, ax = plt.subplots()

# Store minimum values
min_values = []

# Store labels
labels = []

# Iterate over scenarios
for i, scenario in enumerate(scenarios):
    risk_averse, reward_seeking = scenario
    x0 = np.array([0.5, 0.5]) # initial guess

    # Calculate the minimum value for this scenario
    result = scipy.optimize.minimize(f, x0, bounds=bounds, args=(risk_averse, reward_seeking))
    min_values.append(result.fun)
    labels.append(f'Scenario {i+1}')

# Add bars to the chart
ax.bar(labels, min_values, color='blue')

# Set axis labels and title
ax.set_ylabel('Minimum Function Value')
ax.set_xlabel('Scenarios')
ax.set_title('Risk-Reward Analysis')

# Display the chart
plt.show()