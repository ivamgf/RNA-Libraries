import random

class Perceptron:
    def __init__(self, learning_rate=0.1):
        # Inicializa os pesos com valores aleatórios
        self.weights = [random.random() for _ in range(3)]
        # Define o bias
        self.bias = random.random()
        # Define a taxa de aprendizado
        self.learning_rate = learning_rate

    def predict(self, inputs):
        # Multiplica cada entrada pelos seus pesos correspondentes
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs))
        # Adiciona o bias
        weighted_sum += self.bias
        # Retorna a previsão final (1 se o resultado for positivo, -1 se negativo)
        return 1 if weighted_sum >= 0 else -1

    def train(self, inputs, target):
        # Faz a previsão com os pesos atuais
        output = self.predict(inputs)
        # Atualiza os pesos e o bias usando a regra de Hebb
        self.weights = [w + self.learning_rate * x * target for w, x in zip(self.weights, inputs)]
        self.bias += self.learning_rate * target

perceptron = Perceptron()
inputs = [[0.5, -1.2, 0.8], [-0.3, 0.9, -0.1], [0.7, 0.2, -0.5]]
targets = [1, -1, 1]

for i in range(len(inputs)):
    perceptron.train(inputs[i], targets[i])

# Teste a RNA com novos valores de entrada
test_inputs = [0.9, -0.7, 0.3]
output = perceptron.predict(test_inputs)

# Expected output: 1 or -1 (depending on weights and biases updated during training)
print(output)
