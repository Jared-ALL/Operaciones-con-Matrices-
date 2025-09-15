# Importamos la librería Sympy para elaborar las matrices
import sympy as sp

# Definimos la Matriz A de tamaño 3x3.
A = sp.Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Mostramos la matriz A en formato de filas y columnas.
print("Matriz A:")
sp.pprint(A)

# Calculamos el Determinante de la Matriz A.
det_A = A.det()
print("El determinante de A es: ", det_A)

# Creamos una copia de A para no modificar la matriz original.
C = A.copy()

# caso de f = 1e-5
print("\n====== caso f = 1e-5 ======\n")
f = 1e-5

# Modificamos el elemento de la posición (3,3) en la matriz C.
# En Python los índices comienzan en 0, por lo tanto (3,3) corresponde a [2,2].
C[2, 2] = A[2, 2] + f

# Mostramos la nueva matriz C.
print("Matriz C (con el incremento f en la última entrada):")
sp.pprint(C)

# Calculamos el determinante de la matriz C
det_C = C.det()
print("El determinante de C es: ", det_C)

# Verificamos que C es invertible, entonces calculamos la inversa de la matriz
inv_C = C.inv()
print("La inversa de C es:")
sp.pprint(inv_C)

# Definimos el vector b correspondiente al sistema C*y = b
# Observa que el último elemento depende de f para que la solución exacta siga siendo x = [1,1,1]
b = sp.Matrix([
    [6],
    [15],
    [24+f]
])

# Resolvemos el sistema multiplicando la inversa de C por b
# Esto nos da la solución calculada y para el sistema
y = inv_C * b

# Definimos la solución exacta conocida del sistema
x = sp.Matrix([1, 1, 1])

# Calculamos la diferencia entre la solución exacta y la calculada
# Esto nos permite ver qué tan cerca está y de x
z = x - y

 # Mostramos los resultados
print("Vector b:")
sp.pprint(b)
print("Solución calculada y:")
sp.pprint(y)
print("Diferencia z = x - y:")
sp.pprint(z)


# caso de f = 1e-7
print("\n====== caso f = 1e-7 ======\n")
C = A.copy()
f = 1e-7
C[2, 2] = A[2, 2] + f

print("Matriz C (con el incremento f en la última entrada):")
sp.pprint(C)

det_C = C.det()
print("El determinante de C es: ", det_C)

inv_C = C.inv()
print("La inversa de C es:")
sp.pprint(inv_C)

# Definimos el vector b correspondiente al sistema C*y = b
# Observa que el último elemento depende de f para que la solución exacta siga siendo x = [1,1,1]
b = sp.Matrix([
    [6],
    [15],
    [24+f]
])

# Resolvemos el sistema multiplicando la inversa de C por b
# Esto nos da la solución calculada y para el sistema
y = inv_C * b

# Definimos la solución exacta conocida del sistema
x = sp.Matrix([1, 1, 1])

# Calculamos la diferencia entre la solución exacta y la calculada
# Esto nos permite ver qué tan cerca está y de x
z = x - y
 # Mostramos los resultados
print("Vector b:")
sp.pprint(b)
print("Solución calculada y:")
sp.pprint(y)
print("Diferencia z = x - y:")
sp.pprint(z)

# Caso de f = 1e-10
print("\n====== caso f = 1e-10 ======\n")
C = A.copy()
f = 1e-10
C[2, 2] = A[2, 2] + f

print("Matriz C (con el incremento f en la última entrada):")
sp.pprint(C)

det_C = C.det()
print("El determinante de C es: ", det_C)

inv_C = C.inv()
print("La inversa de C es:")
sp.pprint(inv_C)

# Definimos el vector b correspondiente al sistema C*y = b
# Observa que el último elemento depende de f para que la solución exacta siga siendo x = [1,1,1]

b= sp.Matrix([
    [6],
    [15],
    [24+f]
])

# Resolvemos el sistema multiplicando la inversa de C por b
# Esto nos da la solución calculada y para el sistema

y =  inv_C * b

# Definimos la solución exacta conocida del sistema
x = sp.Matrix([1, 1, 1])

# Calculamos la diferencia entre la solución exacta y la calculada
# Esto nos permite ver qué tan cerca está y de x
z = x - y

 # Mostramos los resultados
print("Vector b:")
sp.pprint(b)
print("Solución calculada y:")
sp.pprint(y)
print("Diferencia z = x - y:")
sp.pprint(z)

# Al calcular la inversa de C con f=1e-5, 1e-7 y 1e-10
# se ve que mientras los elementos de C siguen siendo del orden de 1 a 10
# los de inv(C) crecen muchísimo: 1e-5, 1e-7 y 1e-10 respectivamente.
# Esto muestra que, cuanto más pequeño es f, C está más cerca de no ser invertible
# y su inversa se vuelve muy inestable.