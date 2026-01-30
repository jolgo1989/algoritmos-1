# Diferencia entre while y for
# for se usa cuando conoces de antemano la secuencia o el número de iteraciones, mientras que while se emplea cuando quieres repetir un bloque de código mientras se cumpla una condición lógica, sin saber necesariamente cuántas veces ocurrirá.

# la x es la variable de control del bucle.
# for x in range(101):
#     print(x)

# Imprimir rangos específicos
# for x in range(20, 31):
#     print(x)

# Imprimir números impares del 1 al 100
for x in range(1, 100, 2):
    print(x)

# Cómo funciona range(start, stop, step)
# start => valor inicial (incluido).
# stop => valor final (excluido).
# step => incremento entre cada valor.

# ? Desarrollar un programa que permita la carga de 5 valores por teclado y nos muestre posteriormente la suma de los valores ingresados

# suma = 0  # Acumulador para la suma

# for i in range(5):
#     valor = int(input(f"Ingrese el valor {i+1}: "))
#     suma += valor  # Se acumula cada valor ingresado

# print("La suma de los valores ingresados es:", suma)

# ? Desarrollar un programa que permita que el usuario determine cuantos valores por teclado se desea ingresar y nos muestre posteriormente la suma de los valores ingresados.

# num_valores = int(input("¿Cuántos valores desea ingresar? "))
# suma = 0  # Acumulador para la suma

# for i in range(num_valores):
#     valor = int(input(f"Ingrese el valor {i+1}: "))
#     suma += valor  # Se acumula cada valor ingresado

# print("La suma de los valores ingresados es:", suma)


# ? Escribe un programa en Python que pida al usuario un número entero y muestre su tabla de multiplicar del 1 al 10 utilizando un bucle for.

# n = int(input("Ingresa un número: "))
# # Generar la tabla de multiplicar del 1 al 10
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# ? Escribe un programa que permita al usuario ingresar 5 números por teclado. El programa debe calcular y mostrar el promedio de esos valores

# suma = 0  # Acumulador para la suma

# for i in range(5):
#     numero = float(input(f"Ingrese el número {i+1}: "))
#     suma += numero

# promedio = suma / 5
# print("El promedio de los números ingresados es:", promedio)