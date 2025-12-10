"""
Using your Neuron class, simulate a simple neural network with two inputs, 1 hidden layer with 2 nodes, and a single output. Initialize the 3 values that will be inputted in the neural network (x1, x2 and b).
"""

import math


class Neuron:
	
	def __init__(self, w1, w2, activ_fn):
		self.w1 = w1
		self.w2 = w2
		self.activation_function = activ_fn
	
	def run(self, x1, x2, b):
		dot = x1 * self.w1 + x2 * self.w2 + b
		return self.activation_function(dot)


def sigmoid(x):
	return 1 / (1 + math.pow(math.e, x * -1))


def relu(x):
	return max(0, x)



x1 = 0
x2 = 1
b = 1

hidden_neuron1 = Neuron(1, 2, sigmoid)
hidden_neuron2 = Neuron(3, 1, sigmoid)
output_neuron = Neuron(3, 5, relu)

hidden1_output = hidden_neuron1.run(x1, x2, b)
hidden2_output = hidden_neuron2.run(x1, x2, b)

output = output_neuron.run(hidden1_output, hidden2_output, b)

print(hidden1_output)
print(hidden2_output)
print(output)
