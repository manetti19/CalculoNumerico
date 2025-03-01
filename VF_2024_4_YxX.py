import numpy as np
import matplotlib.pyplot as plt

# Constantes
w = 7.29 * (10**(-5))
g = 9.8
L = 67
k = np.sqrt(g / L)

# Condições iniciais
x0 = 0.1
y0 = 0
vx0 = 0
vy0 = 0

# Parâmetros de integração
t0 = 0
tf = 300
dt = 0.1
N = int((tf - t0) / dt)

# Arrays para armazenar os resultados
t = np.linspace(t0, tf, N)
x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)

# Condições iniciais
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

# Função para calcular as derivadas (EDOs de segundo ordem)
def equations(y, t):
    x, y, vx, vy = y
    dxdt = vx
    dydt = vy
    dvxdt = 2 * w * np.sin(np.radians(48.8566)) * vy - k**2 * x
    dvydt = -2 * w * np.cos(np.radians(48.8566)) * vx - k**2 * y

    return [dxdt, dydt, dvxdt, dvydt]

# Método Runge-Kutta de quarta ordem
for i in range(N-1):
    k1 = dt * np.array(equations([x[i], y[i], vx[i], vy[i]], t[i]))
    k2 = dt * np.array(equations([x[i] + 0.5 * k1[0], y[i] + 0.5 * k1[1], vx[i] + 0.5 * k1[2], vy[i] + 0.5 * k1[3]], t[i] + 0.5 * dt))
    k3 = dt * np.array(equations([x[i] + 0.5 * k2[0], y[i] + 0.5 * k2[1], vx[i] + 0.5 * k2[2], vy[i] + 0.5 * k2[3]], t[i] + 0.5 * dt))
    k4 = dt * np.array(equations([x[i] + k3[0], y[i] + k3[1], vx[i] + k3[2], vy[i] + k3[3]], t[i] + dt))

    x[i+1] = x[i] + (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
    y[i+1] = y[i] + (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
    vx[i+1] = vx[i] + (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2]) / 6
    vy[i+1] = vy[i] + (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3]) / 6

# Plotando a curva y = f(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y(t) em função de x(t)')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('Gráfico de y(t) por x(t)')
plt.legend()
plt.grid(True)
plt.show()