import numpy as np

def inversa_matriz(matriz):
    try:
        # Calcula a inversa da matriz usando numpy.linalg.inv
        inversa = np.linalg.inv(matriz)
        return inversa
    except np.linalg.LinAlgError:
        return "A matriz não é inversível."

# Exemplo de uso
# Definindo uma matriz 2x2
matriz = np.array([[1, 2], [3, 4]])             #EXEMPLO

# Calculando a inversa da matriz
inversa = inversa_matriz(matriz)
A=inversa + matriz
print("Matriz inversa:")
print(inversa)

print(A)

