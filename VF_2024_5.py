import numpy as np
import matplotlib.pyplot as plt

# Define a função que representa a equação
def g(r):
    r2 = r * r
    r3 = r * r2
    r4 = r * r3
    return r4 - r2 - 10*(-1/12) + 10*(2/3)*r - 10*(5/12)*r2

# Gera pontos no plano complexo com módulo 1
theta = np.linspace(0, 2*np.pi, 1000)
r_real = np.cos(theta)
r_imag = np.sin(theta)
r_complex = r_real + 1j * r_imag

# Avalia a função para esses pontos
g_values = g(r_complex)

# Separa as partes real e imaginária dos valores da função
g_real_part = np.real(g_values)
g_imag_part = np.imag(g_values)

# Plota o gráfico
plt.figure(figsize=(8, 6))
plt.scatter(g_real_part, g_imag_part, label='Pontos satisfeitos pela equação')
plt.title('Gráfico da Equação para números complexos de módulo 1')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.legend()
plt.grid(True)
plt.show()