import math

# Coordenadas fornecidas (sanha)
X = 596915.961
Y = -4847845.536
Z = 4088158.163
a = 6378137.0
b = 6356752.3142
tolerancia = 1e-6

# W
W = math.sqrt(X**2 + Y**2)

# Chute inicial
m0 = (a * b * (a**2 * Z**2 + b**2 * W**2)**(3/2) - a**2 * b**2 * (a**2 * Z**2 + b**2 * W**2)) / (2 * (a**4 * Z**2 + b**4 * W**2))

# f(m)
def f(m):
    term1 = (W / (a + (2 * m / a)))**2
    term2 = (Z / (b + (2 * m / b)))**2
    return term1 + term2 - 1

#f'(m)
def f_deriv(m):
    term1 = -(2 * W**2) / (a * (a + 2 * m / a)**3)
    term2 = -(2 * Z**2) / (b * (b + 2 * m / b)**3)
    return term1 + term2

#Newton-Raphson
def newton_raphson(m0, tol):
    m = m0
    while abs(f(m)) > tol:
        m = m - f(m) / f_deriv(m)
    return m

#graus decimais para graus, minutos e segundos
def decimal_to_dms(degrees_decimal):
    degrees = int(degrees_decimal)
    minutes_decimal = abs(degrees_decimal - degrees) * 60
    minutes = int(minutes_decimal)
    seconds = (minutes_decimal - minutes) * 60
    return degrees, minutes, seconds

m = newton_raphson(m0, tolerancia)

# Calcular coord. geodésicas
We = W / (1 + 2 * m / a**2)
Xe = X / (1 + 2 * m / a**2)
Ye = Y / (1 + 2 * m / a**2)
Ze = Z / (1 + 2 * m / b**2)

# Latitude
phi = math.degrees(math.atan((a**2 * Ze) / (b**2 * We)))

# Longitude
lambd = math.degrees(math.atan(Y / X))

W_novo = math.sqrt(Xe**2 + Ye**2)

# Altitude
h = math.sqrt((W_novo - We)**2 + (Z - Ze)**2)
if (W_novo + abs(Z)) < (We + abs(Ze)):
    h = -h


phi_degrees, phi_minutes, phi_seconds = decimal_to_dms(phi)
lambda_degrees, lambda_minutes, lambda_seconds = decimal_to_dms(lambd)

def main():
    print(f"Latitude (φ): {phi_degrees}° {phi_minutes}' {phi_seconds:.4f}''")
    print(f"Longitude (λ): {lambda_degrees}° {lambda_minutes}' {lambda_seconds:.4f}''")
    print(f"Altitude (h): {h:.4f} metros")
    
main()



