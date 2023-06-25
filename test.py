import tensorflow as tf

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values to a range of 0 to 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Create a sequential neural network model
model = tf.keras.models.Sequential([
    # Flatten the input images from 2D to 1D
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    # Add a dense layer with 128 units and ReLU activation
    tf.keras.layers.Dense(128, activation='relu'),
    # Apply dropout regularization with a rate of 0.2
    tf.keras.layers.Dropout(0.2),
    # Add the output layer with 10 units and softmax activation
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model with the specified optimizer, loss function, and metrics
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model on the training dataset for 5 epochs
model.fit(x_train, y_train, epochs=5)

# Evaluate the model on the test dataset and obtain the loss and accuracy
model.evaluate(x_test, y_test)