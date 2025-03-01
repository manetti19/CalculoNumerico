import numpy as np
import matplotlib.pyplot as plt

# Dimensões da placa
Lx, Ly = 3.0, 3.0

# Parâmetros de discretização espacial e temporal
Nx, Ny = 50, 50  # Resolução da grade
dx, dy = Lx / Nx, Ly / Ny
alpha = 0.05
T = 2.0
dt = 0.01
Nt = int(T / dt)

# Criação das coordenadas x, y
x = np.linspace(-3, 3, Nx)
y = np.linspace(-3, 3, Ny)

# Configuração inicial de temperatura
# Usar os dados fornecidos para preencher a matriz inicial da borda
temp_start = np.array([-10, 0, 5, 20, 50, 30, 15])

# Configuração inicial
u = np.zeros((Nx, Ny))

# Mapeando os valores de temperatura para o plano considerando eixo x
u[:, 0] = np.interp(x, np.linspace(-3, 3, len(temp_start)), temp_start)

# Criando a matriz para armazenar a nova temperatura
u_new = np.copy(u)

# Plotando a condição inicial
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(u, extent=[-3, 3, -3, 3], origin='lower', cmap='hot')
plt.colorbar()
plt.title('Condição Inicial')
plt.xlabel('x')
plt.ylabel('y')

# Loop no tempo para evolução
for n in range(Nt):
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            # Aplicar equação de calor
            u_new[i, j] = u[i, j] + alpha * dt * (
                (u[i+1, j] - 2*u[i, j] + u[i-1, j]) / dx**2 +
                (u[i, j+1] - 2*u[i, j] + u[i, j-1]) / dy**2
            )
    u = u_new.copy()

# Plotando a condição final após T segundos
plt.subplot(1, 2, 2)
plt.imshow(u, extent=[-3, 3, -3, 3], origin='lower', cmap='hot')
plt.colorbar()
plt.title('Temperatura após 2 segundos')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.show()
