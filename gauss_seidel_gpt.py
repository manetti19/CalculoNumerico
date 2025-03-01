import numpy as np

def gauss_seidel(A, b, x0, tol=1e-10, max_iterations=1000):
    n = len(b)
    x = x0.copy()
    
    for iteration in range(max_iterations):
        x_new = x.copy()
        
        for i in range(n):
            # Calcula a soma do produto dos coeficientes com as soluções anteriores
            sum_ = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            # Atualiza imediatamente o valor de x[i]
            x_new[i] = (b[i] - sum_) / A[i][i]

        # Verifica a convergência
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f'Convergência alcançada após {iteration + 1} iterações.')
            return x_new
        
        x = x_new

    print('Número máximo de iterações alcançado.')
    return x

# Exemplo de uso
A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]])

b = np.array([15, 10, 10, 10])
x0 = np.zeros_like(b)

# Calcula a solução usando o método de Gauss-Seidel
solution = gauss_seidel(A, b, x0)
print('Solução:')
print(solution)
