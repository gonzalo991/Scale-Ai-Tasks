# Define a function to find the maximum and minimum values
f = @(x) x.^2;

# Find the minimum value
[min_value, min_location] = fminbnd(f, -10, 10);

# Find the maximum value by finding the minimum of the negative of the function
f_neg = @(x) -f(x);
[max_value_neg, max_location] = fminbnd(f_neg, -10, 10);
max_value = -max_value_neg;

# Print the minimum and maximum values
disp(min_value);
disp(max_value);