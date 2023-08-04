import scipy.optimize
import numpy as np

def f(x):
    return x[0]**2 + x[1]**2

x0 = np.array([2, 2])

#Define bounds for x and y 
bounds = scipy.optimize.Bounds([-10,-10],[10,10])

result = scipy.optimize.minimize(f, x0, bounds = bounds)

print(f"The minimum value is: {result.fun}")
print(f"The minimum is located at: {result.x}")