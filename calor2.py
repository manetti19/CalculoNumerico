import numpy as np
import matplotlib.pyplot as plt

# Definições iniciais
L = 5.0  # Comprimento da barra em metros
n_points = 10  # Número de pontos
x = np.linspace(0, L, n_points)  # Posições ao longo da barra
temperaturas_iniciais = np.array([-50, 0, 50, 100, 150, 300, 500, 400, 200, -100])  # Temperaturas iniciais

# Parâmetros da simulação
k = 1.0  # Difusividade térmica (ajustável conforme necessário)
delta_x = x[1] - x[0]  # Espaçamento entre os pontos
delta_t = 0.2  # Passo de tempo
steps = 2  # Número de passos de tempo

# Gráfico da temperatura inicial
plt.figure(figsize=(12, 5))

# Gráfico inicial
plt.subplot(1, 2, 1)
plt.plot(x, temperaturas_iniciais, marker='o', linestyle='-', color='b', label='Temperatura inicial')
plt.title('Temperaturas Iniciais ao Longo da Barra')
plt.xlabel('Posição na barra (m)')
plt.ylabel('Temperatura (°C)')
plt.grid()
plt.legend()

# Usando a equação de calor para calcular temperaturas após ∆t
temperaturas = np.copy(temperaturas_iniciais)

for n in range(steps):
    # Aplique a equação de calor, considerando que a borda não muda
    novas_temperaturas = np.copy(temperaturas)
    for i in range(1, n_points - 1):
        novas_temperaturas[i] = temperaturas[i] + (k * delta_t / delta_x**2) * (temperaturas[i + 1] - 2 * temperaturas[i] + temperaturas[i - 1])
    
    temperaturas = novas_temperaturas  # Update temperatures for next iteration

# Gráfico após um passo de tempo
plt.subplot(1, 2, 2)
plt.plot(x, temperaturas, marker='o', linestyle='-', color='r', label='Temperatura após ∆t')
plt.title(f'Temperaturas Após {delta_t} Tempo')
plt.xlabel('Posição na barra (m)')
plt.ylabel('Temperatura (°C)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# Encontrando os zeros da equação (aproximadamente)
zeros = np.where(np.diff(np.sign(temperaturas)))[0]

# Exibindo as posições dos zeros
if len(zeros) > 0:
    zero_positions = x[zeros] + (x[zeros + 1] - x[zeros]) / 2  # Encontra a posição aproximada de zero
    print(f"As posições aproximadas de zeros são: {zero_positions}")
else:
    print("Não há zeros nas temperaturas calculadas.")
