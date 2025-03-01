import numpy as np
import matplotlib.pyplot as plt

# Constantes
b = 10 / (24 * 40 * 8)
c = 3 / (15 * 24)

# Intervalo de tempo
t0, tf = 0, 700
dt = 700 / 199
t = np.arange(t0, tf + dt, dt)

# Condições iniciais
S0, I0, R0 = 50, 1, 0

# Inicialização das soluções
S = np.zeros_like(t)
I = np.zeros_like(t)
R = np.zeros_like(t)
S[0], I[0], R[0] = S0, I0, R0

# Implementação do método de Euler
for i in range(1, len(t)):
    S[i] = S[i - 1] + (-b * S[i - 1] * I[i - 1]) * dt
    I[i] = I[i - 1] + (b * S[i - 1] * I[i - 1] - c * I[i - 1]) * dt
    R[i] = R[i - 1] + (c * I[i - 1]) * dt

# Plot dos resultados
plt.figure(figsize=(12, 8))
plt.plot(t, S, label='S')
plt.plot(t, I, label='I')
plt.plot(t, R, label='R')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Modelo SEIR usando Euler')
plt.legend()
plt.grid(True)
plt.show()