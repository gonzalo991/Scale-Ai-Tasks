import matlab
import numpy as np
import matplotlib.pyplot as plt

# Define the MATLAB code
matlab_code = """
function plot_data(data)
    plot(data(1:100), data(101:end));
    title('Data visualization with MATLAB');
    xlabel('Time steps');
    ylabel('Output value');
end
"""

# Generate some sample data
data = np.random.rand(200)

# Run the MATLAB code
eng = matlab.engine.start_matlab()
eng.eval(matlab_code)
eng.plot_data(data.tolist(), nargout=0)

# Display the plot
plt.show()
