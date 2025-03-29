# Perceptron as Logical Operators
# AND operator

# Import the necessary libraries
import pandas as pd

# Define the inputs, expected outputs from Perceptron
inputs = [(0,0), (1,0), (0,1), (1,1)]
expected_outputs = [False, False, False, True]


# Guess the weights
weight_1 = 1
weight_2 = 1
bias = 0

actual_outputs = []
for input, expected_outputs in zip(inputs, expected_outputs):
    linear_combination = input[0]*weight_1 + input[1]*weight_2 + bias
    if linear_combination < 0:
        result = False
    else:
        result = True
    actual_outputs.append(result)

print(actual_outputs)
