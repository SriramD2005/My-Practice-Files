import random
import math

# 🔧 Activation functions
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 🧱 Layer class
class Layer:
    def __init__(self, input_size, output_size):
        self.weights = [[random.uniform(-1, 1) for _ in range(input_size)] for _ in range(output_size)]
        self.biases = [random.uniform(-1, 1) for _ in range(output_size)]
        self.outputs = [0] * output_size
        self.deltas = [0] * output_size

    def forward(self, inputs):
        self.inputs = inputs
        self.outputs = []
        for i in range(len(self.weights)):
            activation = sum(w * inp for w, inp in zip(self.weights[i], inputs)) + self.biases[i]
            self.outputs.append(sigmoid(activation))
        return self.outputs

    def backward(self, next_weights, next_deltas):
        for i in range(len(self.outputs)):
            error = sum(next_weights[j][i] * next_deltas[j] for j in range(len(next_deltas)))
            self.deltas[i] = error * sigmoid_derivative(self.outputs[i])

    def update(self, learning_rate):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                self.weights[i][j] += learning_rate * self.deltas[i] * self.inputs[j]
            self.biases[i] += learning_rate * self.deltas[i]

# 🧠 MLP class
class MLP:
    def __init__(self, layers):
        self.layers = []
        for i in range(len(layers) - 1):
            self.layers.append(Layer(layers[i], layers[i+1]))

    def forward(self, inputs):
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs

    def backward(self, expected):
        # Output layer delta
        last = self.layers[-1]
        for i in range(len(last.outputs)):
            error = expected[i] - last.outputs[i]
            last.deltas[i] = error * sigmoid_derivative(last.outputs[i])
        # Hidden layers delta
        for i in reversed(range(len(self.layers) - 1)):
            self.layers[i].backward(self.layers[i+1].weights, self.layers[i+1].deltas)

    def update(self, learning_rate):
        for layer in self.layers:
            layer.update(learning_rate)

    def train(self, data, labels, epochs=1000, lr=0.1):
        for epoch in range(epochs):
            total_loss = 0
            for x, y in zip(data, labels):
                output = self.forward(x)
                self.backward(y)
                self.update(lr)
                total_loss += sum((o - t) ** 2 for o, t in zip(output, y))
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

# 🧪 Ritualized test
if __name__ == "__main__":
    # XOR dataset
    data = [[0,0], [0,1], [1,0], [1,1]]
    labels = [[0], [1], [1], [0]]

    mlp = MLP([2, 4, 1])
    mlp.train(data, labels, epochs=1000, lr=0.1)

    for x in data:
        print(f"Input: {x}, Output: {mlp.forward(x)}")