import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense
from tensorflow.keras.models import Sequential

# Define a new layer class
class NewLayer(Layer):
    def __init__(self, num_neurons, **kwargs):
        super(NewLayer, self).__init__(**kwargs)
        self.num_neurons = num_neurons

    def build(self, input_shape):
        #Initialize the build for each neuron
        self._weights = self.add_weight(shape=(input_shape[-1], self.num_neurons),
                                        initializer='random_normal',
                                        trainable=True)

        # Initialize the bias (threshold in your neuron terminology)
        self._biases = self.add_weight(shape=(self.num_neurons,),
                                        initializer='zeros',
                                        trainable=True)

    def call(self, inputs):
    # Compute the dot product of weights and inputs, and add the bias
        outputs = tf.matmul(inputs, self._weights) + self._biases
        # Apply the activation function (sigmoid in this case) to the outputs
        outputs = tf.sigmoid(outputs)
        return outputs

# Define the model
model = Sequential([
# First hidden layer with sigmoid activation function
NewLayer(16),

# Second hidden layer
NewLayer(16),
Dense(10, activation='softmax')
])

# Define the optimizer, loss function and metrics
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Summary of the model
model.summary()