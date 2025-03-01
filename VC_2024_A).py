import numpy as np

# Funções de sistema não linear (equações)
def sistema(vars):
    phi, lamb = vars  # phi = latitude, lamb = longitude

    # Conversões de unidades
    h1 = np.radians(38 + 22/60 + 32.43/3600)
    h2 = np.radians(35 + 8/60 + 28.66/3600)

    delta1 = np.radians(-(53 + 40/60 + 71.95/3600))
    delta2 = np.radians(-(16 + 41/60 + 29.39/3600))

    alpha1 = 6 + 23/60 + 33.771/3600
    alpha2 = 6 + 44/60 + 19.230/3600

    UT1 = 23 + 4/60 + 22.34/3600
    UT2 = 23 + 15/60 + 16.46/3600

    theta0 = 6 + 22/60 + 30.977/3600

    # Ângulos horários t1 e t2 ( faça uma funçao para calcula-los aqui)

    t1 = 1.0027379*UT1 + theta0 - alpha1 - np.degrees(lamb) / 15.0  # Convertendo lamb de radianos para horas
    t2 = 1.0027379*UT2 + theta0 - alpha2 - np.degrees(lamb) / 15.0  # Convertendo lamb de radianos para horas

    # Convertendo t para radianos
    t1 = np.radians(t1 * 15)  # Convertendo de horas para graus e depois para radianos
    t2 = np.radians(t2 * 15)

    # Ajuste do sinal de t: se o cosseno for negativo, a estrela está a oeste e t deve ser positivo
    if np.cos(t1) < 0:
        t1 = 2 * np.pi - t1
    if np.cos(t2) < 0:
        t2 = 2 * np.pi - t2

    # Sistema de equações
    eq1 = np.cos(t1) - (np.sin(h1)-np.sin(delta1)*np.sin(phi))/(np.cos(delta1)*np.cos(phi))
    eq2 = np.cos(t2) - (np.sin(h2)-np.sin(delta2)*np.sin(phi))/(np.cos(delta2)*np.cos(phi))

    return np.array([eq1, eq2])

# Função para calcular a Jacobiana numericamente
def jacobiana(f, vars, h=1e-5):
    n = len(vars)
    J = np.zeros((n, n))
    f0 = f(vars)

    for i in range(n):
        vars_h = np.copy(vars)
        vars_h[i] += h
        f_h = f(vars_h)
        J[:, i] = (f_h - f0) / h

    return J

# Método de Newton-Raphson
def newton_raphson(f, vars_iniciais, tol, max_iter=100):
    vars = np.array(vars_iniciais,dtype=float)
    for i in range(max_iter):
        f_val = f(vars)
        J = jacobiana(f, vars)
        delta_vars = np.linalg.solve(J, -f_val)
        vars = vars + delta_vars

        # Critério de parada: precisão da longitude em segundos de arco
        if np.abs(delta_vars[1]) < tol:  # Tolera longitude em arcseconds
            break

    return vars

# Definindo valores iniciais aproximados para phi e lambda (Rio de Janeiro)
phi0 = np.radians(-22)  # Aproximadamente a latitude do Rio de Janeiro
lambda0 = np.radians(45)  # Aproximadamente a longitude do Rio de Janeiro

# Critério de parada: 1/1000 de segundo de arco (em radianos)
#tol = np.radians(1 / (1000 * 3600))
tol = np.radians(0.000000278)
# Função para converter decimal em graus, minutos e segundos com o sinal correto
def decimal_para_graus_min_seg(angle):
    graus = int(angle)
    minutos_dec = abs((angle - graus) * 60)
    minutos = int(minutos_dec)
    segundos = (minutos_dec - minutos) * 60
    return graus, minutos, segundos

# Resolvendo o sistema com o programa anterior
solucao = newton_raphson(sistema, [phi0, lambda0], tol)

# Convertendo a solução para graus
phi_sol = np.degrees(solucao[0])  # Latitude
lambda_sol = np.degrees(solucao[1]) % 360  # Longitude no intervalo [0°, 360°]

# Ajustando a longitude: se > 180, significa Oeste
if lambda_sol > 180:
    lambda_sol = 360 - lambda_sol
    longitude_direcao = "Oeste"
else:
    longitude_direcao = "Leste"

# Convertendo latitude e longitude para graus, minutos e segundos
phi_graus, phi_minutos, phi_segundos = decimal_para_graus_min_seg(phi_sol)
lambda_graus, lambda_minutos, lambda_segundos = decimal_para_graus_min_seg(lambda_sol)

# Ajustando o sinal da latitude (negativa para o Hemisfério Sul)
if phi_sol < 0:
    latitude_direcao = "Sul"
else:
    latitude_direcao = "Norte"

# Imprimindo os resultados
print(f"Latitude (phi): {abs(phi_graus)}° {phi_minutos}' {phi_segundos:.3f}'' {latitude_direcao}")
print(f"Longitude (lambda): {lambda_graus}° {lambda_minutos}' {lambda_segundos:.3f}'' {longitude_direcao}")
