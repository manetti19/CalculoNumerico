import numpy as np
import matplotlib.pyplot as plt

# Valores dados
x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = np.array([-10, 0, 5, 20, 50, 30, 15])

# Interpolação polinomial
# O grau do polinômio é igual a número de pontos - 1
degree = len(x) - 1
coefficients = np.polyfit(x, y, degree)
polynomial = np.poly1d(coefficients)

# Criando novos pontos para plotagem
x_interp = np.linspace(-3, 3, 300)
y_interp = polynomial(x_interp)

# Plotando os dados originais e a curva interpolada
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='Dados Originais')
plt.plot(x_interp, y_interp, color='red', linestyle='--', label='Polinômio Interpolador')

plt.title('Interpolação Polinomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()

plt.show()

# Coeficientes do polinômio
print("Coeficientes do polinômio (do maior ao menor grau):", coefficients)
