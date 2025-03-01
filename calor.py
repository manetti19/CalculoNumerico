import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
Lx, Ly = 6.0, 6.0  # Tamanho do plano (de -3 a 3)
T = 1.0  # Tempo total aumentado
alpha = 0.05  # Difusividade térmica
Nx, Ny = 100, 100  # Resolução espacial
Nt = 50000  # Aumentado o número de passos de tempo

dx = Lx / (Nx + 1)
dy = Ly / (Ny + 1)
dt = T / Nt
x = np.linspace(-3, 3, Nx + 2)  # Variando de -3 a 3
y = np.linspace(-3, 3, Ny + 2)  # Variando de -3 a 3

# Condições iniciais - temperatura ao longo do lado esquerdo, variando como uma senoide
u_initial = np.zeros((Nx + 2, Ny + 2))
u_initial[:, 0] = np.sin(np.pi * y)  # Senoide variando ao longo do lado esquerdo

# Clonando condição inicial para evolução
u = u_initial.copy()

# Plotando a condição inicial
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(u_initial, extent=[-3, 3, -3, 3], origin='lower', cmap='hot', aspect='auto', vmin=-1, vmax=1)
plt.colorbar()
plt.title('Condição Inicial')
plt.xlabel('x')
plt.ylabel('y')

# Loop no tempo para evolução
for n in range(Nt):
    u_new = u.copy()
    # Atualização das soluções internas
    u_new[1:-1, 1:-1] = u[1:-1, 1:-1] + alpha * dt * (
        (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx**2 +
        (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dy**2
    )
    u = u_new

# Plotando a condição final
plt.subplot(1, 2, 2)
plt.imshow(u, extent=[-3, 3, -3, 3], origin='lower', cmap='hot', aspect='auto', vmin=-1, vmax=1)
plt.colorbar()
plt.title('Final')
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
plt.show()
