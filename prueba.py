import matplotlib.pyplot as plt

# Función para calcular la serie de Fibonacci
def fibonacci(n):
    """
    Genera la secuencia de Fibonacci hasta el enésimo término.

    :param n: Número de términos de la secuencia a generar.
    :return: Lista con la secuencia de Fibonacci.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Número de términos de Fibonacci a calcular
n_terms = 10
fib_sequence = fibonacci(n_terms)

# Representar la serie de Fibonacci
plt.plot(fib_sequence, marker='o')
plt.title('Serie de Fibonacci')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid()

# Guardar la figura en un archivo PNG
plt.savefig('fibonacci.png')

plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    num_terms = int(input("Introduce el número de términos de la secuencia de Fibonacci: "))
    print(f"Secuencia de Fibonacci: {fibonacci(num_terms)}")