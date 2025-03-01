import numpy as np
import matplotlib.pyplot as plt

# Dados da tabela
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2, 2.5, 2, 3, 3.5, 4.5, 6, 7])

# Ajuste de curva com polinômio de grau 2 (parábola)
coefs = np.polyfit(x, y, 2)

# Mostra os coeficientes
a, b, c = coefs
print(f"Coeficientes: a = {a}, b = {b}, c = {c}")

# Plota os dados e a curva ajustada
plt.scatter(x, y, color='red', label='Dados')

# Cria valores para x para o gráfico da parábola
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * x_fit**2 + b * x_fit + c

plt.plot(x_fit, y_fit, label='Ajuste parabólico', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste de Parábola aos Dados')
plt.show()
