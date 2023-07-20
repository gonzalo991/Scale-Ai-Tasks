import random
import math

class Neuron:
    def __init__(self, inputs=None, alpha=1.0):
        if inputs:
        # Initialize weights and weight updates
            self._weights = [0] * inputs
            self._weight_updates = [0] * inputs
            self.initial_weights()
        else:
            self._weights = None
            self._weight_updates = None

        # Initialize alpha, threshold, and threshold update
            self._alpha = alpha
            self._threshold = 0
            self._threshold_update = 0
            self._output = 0

    def initial_weights(self):
        # Assign a random number to each weight
        for w in range(len(self._weights)):
            self._weights[w] = random.random()

    def calculate_output(self, inputs):
        # Compute the dot product of weights and inputs, and add the threshold
        sum_ = sum(i*w for i, w in zip(inputs, self._weights))
        # Apply the sigmoid function to the result
        self._output = self.sigmoid(sum_ + self._threshold)
        return self._output

    def sigmoid(self, x):
        # Apply the sigmoid function to x
        return (2 / (1 + math.exp(-self._alpha * x))) - 1

    def sigmoid_derivative(self, x):
        #Compute the derivative of the sigmoid function
        return self._alpha * (1 - (x * x)) / 2

    @property
    def delta(self):
        # Compute delta using the derivative of the sigmoid function
        return self.sigmoid_derivative(self._output)

    def backpropagation(self, inputs, target):
        # Compute the error between the actual output and the target
        error = target - self._output
        # Compute delta using the error and the delta
        delta = error * self.delta
        # Update the weights and threshold using the delta
        self._weight_updates = [dw + i*delta for i, dw in zip(inputs, self._weight_updates)]
        self._threshold_update += delta
        # Apply the updates to the weights and the threshold
        self.apply_updates()

    def apply_updates(self):
        # Apply updates to the weights and threshold
        for w in range(len(self._weights)):
            self._weights[w] += self._weight_updates[w]
            self._threshold += self._threshold_update
        # Reset weight updates and threshold update to 0 for the next round of backpropagation
        self._weight_updates = [0] * len(self._weight_updates)
        self._threshold_update = 0