import numpy as np


# Dados fornecidos
I1 = 2527.967  # kJ/m^2*h
I2 = 4611.454  # kJ/m^2*h

# Horas locais
H1 = 8  # 8h
H2 = 11  # 11h

# Ângulo horário
omega1 = (H1 - 12) * 15  # em graus
omega2 = (H2 - 12) * 15  # em graus

# Convertendo para radianos
omega1 = np.radians(omega1)
omega2 = np.radians(omega2)

# Funções f1(delta, phi) e f2(delta, phi)
def f1(delta, phi):
    return 4921 * (np.sin(delta) * np.sin(phi) + np.cos(delta) * np.cos(phi) * np.cos(omega1)) - I1

def f2(delta, phi):
    return 4921 * (np.sin(delta) * np.sin(phi) + np.cos(delta) * np.cos(phi) * np.cos(omega2)) - I2

# Derivadas parciais em relação a delta e phi
def f1_partial_delta(delta, phi):
    return 4921 * (np.cos(delta) * np.sin(phi) - np.sin(delta) * np.cos(phi) * np.cos(omega1))

def f1_partial_phi(delta, phi):
    return 4921 * (np.sin(delta) * np.cos(phi) - np.cos(delta) * np.sin(phi) * np.cos(omega1))

def f2_partial_delta(delta, phi):
    return 4921 * (np.cos(delta) * np.sin(phi) - np.sin(delta) * np.cos(phi) * np.cos(omega2))

def f2_partial_phi(delta, phi):
    return 4921 * (np.sin(delta) * np.cos(phi) - np.cos(delta) * np.sin(phi) * np.cos(omega2))

# Jacobiana J(delta, phi)
def jacobian(delta, phi):
    return np.array([
        [f1_partial_delta(delta, phi), f1_partial_phi(delta, phi)],
        [f2_partial_delta(delta, phi), f2_partial_phi(delta, phi)]
    ])

# Método de Newton-Raphson para sistemas não lineares
def newton_raphson_multivariate(F, J, delta0, phi0, tol=1e-6, max_iter=100):
    delta, phi = delta0, phi0
    for i in range(max_iter):
        F_val = np.array([F[0](delta, phi), F[1](delta, phi)])
        J_val = J(delta, phi)
        
        # Verifica se a Jacobiana é singular
        if np.linalg.cond(J_val) > 1e10:
            raise ValueError("Jacobiana próxima de singularidade")

        delta_phi_new = np.array([delta, phi]) - np.linalg.solve(J_val, F_val)
        if np.linalg.norm(delta_phi_new - np.array([delta, phi])) < tol:
            return delta_phi_new, i + 1
        delta, phi = delta_phi_new
    raise ValueError("Convergência não alcançada")

# Definindo as funções do sistema
F = [f1, f2]

# Chute inicial (estimativas iniciais para delta e phi em radianos)
delta0 = np.radians(-20)  # Chute inicial para delta (próximo do equinócio)
phi0 = np.radians(-23.5)  # Chute inicial para a latitude (perto da latitude de São Paulo)

# Calculando delta e phi usando Newton-Raphson multidimensional
try:
    delta_phi_sol, iterations = newton_raphson_multivariate(F, jacobian, delta0, phi0)
    # Convertendo delta e phi para graus
    delta_sol_deg, phi_sol_deg = np.degrees(delta_phi_sol)

    print(f"Declinação solar (δ): {delta_sol_deg:.2f}°")
    print(f"Latitude (φ): {phi_sol_deg:.2f}°")
    print(f"Número de iterações: {iterations}")

except ValueError as e:
    print(e)