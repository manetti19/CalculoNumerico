import numpy as np
import matplotlib.pyplot as plt

def edo_heun(f, y0, t0, tf, h):
    """
    Resolve a EDO y' + 2y = 0 usando o método de Heun (Euler modificado)

    :param f: Função que define a derivada dy/dt
    :param y0: Condição inicial y(t0) = y0
    :param t0: Ponto inicial t0
    :param tf: Ponto final tf
    :param h: Tamanho do passo
    :return: Arrays de tempos (t) e soluções (y)
    """
    n = int((tf - t0) / h)
    t = np.linspace(t0, tf, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h, y[i] + h * k1)
        y[i+1] = y[i] + (h / 2) * (k1 + k2)

    return t, y

# Definir a função f que corresponde à EDO y' + 2y = 0
def f(t, y):
    return -2 * y

# Condição inicial e intervalo de tempo
y0 = 1  # Exemplo: y(0) = 1
t0 = 0
tf = 5
h = 0.1

# Resolver a EDO usando o método de Heun
t, y = edo_heun(f, y0, t0, tf, h)

# Plotar o gráfico
plt.figure(figsize=(8, 6))
plt.plot(t, y, label='Solução da EDO')
plt.title('Método de Heun para a EDO y'' + 2y = 0')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()