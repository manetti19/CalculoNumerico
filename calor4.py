import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Dimensões da placa
Lx, Ly = 3.0, 3.0

# Parâmetros de discretização espacial e temporal
Nx, Ny = 50, 50  # Resolução da grade
dx, dy = Lx / Nx, Ly / Ny
alpha = 0.05
T = 10.0  # Tempo estendido para 10 segundos
dt = 0.01
Nt = int(T / dt)

# Coordenadas x, y
x = np.linspace(-3, 3, Nx)
y = np.linspace(-3, 3, Ny)

# Dados de temperatura para y = -3
temp_y = np.array([-3, -2, -1, 0, 1, 2, 3])
temp_values = np.array([-10, 0, 5, 20, 50, 30, 15])

# Criar uma função de interpolação
temp_func = interp1d(temp_y, temp_values, kind='cubic', fill_value="extrapolate")

# Configuração inicial
u_initial = np.zeros((Nx, Ny))
# Aplicar a temperatura ao longo de y = -3 interpolando para cada ponto de x
for j, yj in enumerate(y):
    u_initial[0, j] = temp_func(yj)

# Criando a matriz para armazenar a nova temperatura
u_new = np.copy(u_initial)

# Plotando a distribuição inicial de temperatura
plt.figure(figsize=(18, 10))
plt.subplot(2, 2, 1)
plt.imshow(u_initial, extent=[-3, 3, -3, 3], origin='lower', cmap='hot')
plt.colorbar()
plt.title('Distribuição Inicial de Temperatura na Placa')
plt.xlabel('x')
plt.ylabel('y')

# Simulação de calor no tempo
u = np.copy(u_initial)
for n in range(Nt):
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            # Aplicar equação de calor
            u_new[i, j] = u[i, j] + alpha * dt * (
                (u[i+1, j] - 2*u[i, j] + u[i-1, j]) / dx**2 +
                (u[i, j+1] - 2*u[i, j] + u[i, j-1]) / dy**2
            )
    u = u_new.copy()

# Plotando a condição final da placa após T segundos
plt.subplot(2, 2, 2)
plt.imshow(u, extent=[-3, 3, -3, 3], origin='lower', cmap='hot')
plt.colorbar()
plt.title('Distribuição de Temperatura Após 10 segundos')
plt.xlabel('x')
plt.ylabel('y')

# Plotando a equação de temperatura inicial por x
plt.subplot(2, 2, 3)
y_dense = np.linspace(-3, 3, 300)
plt.plot(temp_y, temp_values, 'o', label='Pontos de Dados')
plt.plot(y_dense, temp_func(y_dense), '-', label='Interpolação Cubic')
plt.title('Interpolação de Temperatura Inicial ao Longo de y=-3')
plt.xlabel('x')
plt.ylabel('Temperatura (°C)')
plt.grid()
plt.legend()



plt.tight_layout()
plt.show()