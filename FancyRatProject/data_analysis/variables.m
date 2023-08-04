% Define data types, variables, and operations

% Data types
double_var = double(0.5);
int8_var = int8(127);
uint16_var = uint16(65535);

% Variables
my_var1 = 5;
my_var2 = my_var1 + 10;

% Operations
my_var3 = my_var2 + 5;
my_var4 = my_var3 * 2;

% Conditionals
if my_var4 > 10
    my_var5 = my_var4 - 10;
else
    my_var5 = my_var4 + 10;
end

% Loops
for i = 1:5
    my_var6(i) = i * 10;
end

% Functions
function my_var7 = my_function1(arg1, arg2)
    my_var7 = arg1 + arg2; % Your code here
end

% Use variables, operations, conditionals, and loops
my_var8 = my_var5 + 10;
for i = 1:5
    my_var9(i) = my_var6(i) + my_var8;
end

% Use function
my_var10 = my_function1(my_var1, my_var2);

% Display results
disp('Data types:');
disp(double_var);
disp(int8_var);
disp(uint16_var);

disp('Variables:');
disp(my_var1);
disp(my_var2);
disp(my_var3);
disp(my_var4);
disp(my_var5);
disp(my_var6);
disp(my_var8);
disp(my_var9);
disp(my_var10);