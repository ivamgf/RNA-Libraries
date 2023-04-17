import random

class Perceptron:
    def __init__(self):
        # Inicializa os pesos com valores aleatórios
        self.weights = [random.random() for _ in range(3)]
        # Define o bias
        self.bias = random.random()

    def predict(self, inputs):
        # Multiplica cada entrada pelos seus pesos correspondentes
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs))
        # Adiciona o bias
        weighted_sum += self.bias
        # Retorna a previsão final (1 se o resultado for positivo, -1 se negativo)
        return 1 if weighted_sum >= 0 else -1

perceptron = Perceptron()
inputs = [0.5, -1.2, 0.8]
output = perceptron.predict(inputs)

# Expected output: 1 or -1 (depending on randomly generated weights and biases)
print(output)
