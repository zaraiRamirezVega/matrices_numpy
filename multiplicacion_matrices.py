import numpy as np

# Crear dos matrices aleatorias de 3x3
matrizA = np.random.randint(1, 10, size=(3, 3))
matrizB = np.random.randint(1, 10, size=(3, 3))

# Mostrar las matrices y su multiplicación
resultado = np.dot(matrizA, matrizB)
print(f'La multiplicación de la Matriz A:\n{matrizA}\ncon la Matriz B:\n{matrizB}\nes igual a:\n{resultado}')
