import math

class Neuron:

  # instance attributes: weights and activation function
  def __init__(self, w1, w2, activ_fn):
    self.w1 = w1
    self.w2 = w2
    self.activation_function = activ_fn

  # passes an input (x1 and x2) into the neuron and returns the neuron's output
  def run(self, x1, x2, b):
    dot = x1*self.w1 + x2*self.w2 + b
    return self.activation_function(dot)

def sigmoid(x):
  return 1/(1 + math.pow(math.e, x*-1))

n = Neuron(1, 2, sigmoid)
print(n.run(0, 1, 1))
