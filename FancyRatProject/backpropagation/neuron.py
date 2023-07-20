import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Number of input features
n_inputs = 10

# Define the model
model = Sequential([
# First hidden layer with sigmoid activation function
Dense(16, input_shape=(n_inputs,), activation='sigmoid'),

# Second hidden layer
Dense(16, activation='sigmoid'),

# Output layer with sigmoid activation function
Dense(1, activation='sigmoid'),
])

# Choose the optimizer, loss function and metrics
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Summary of the model
model.summary()