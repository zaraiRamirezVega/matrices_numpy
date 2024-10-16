import numpy as np

# Crear una matriz aleatoria de 3x4 con números enteros entre 1 y 9
matriz = np.random.randint(1, 10, size=(3, 4))

# Mostrar la matriz original y la nueva matriz después de eliminar la columna 3
print(f'Matriz:\n{matriz}\n')
print(f'La nueva matriz después de eliminar la columna 3 es:\n{np.delete(matriz, 2, axis=1)}')



