"""1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa."""


def suma(a, b):
    return a + b


resultado = suma(10, 2)
print(resultado)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))


def suma_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


Lista_numeros = [1, 8, 4, 6, 3]
print(suma_lista(Lista_numeros))

cadena = "Laura"
cadena_invertida = cadena[::-1]
print(cadena_invertida)

# Ejercicio 3


def num_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(num_primo(8))

# Ejercicio 4


def suma_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


mi_lista = [16, 10, 20, 5]
print(suma_lista(mi_lista))

# Ejercicio 5
capicua = "Somos"
palabra_capicua = capicua[::-1]
print(palabra_capicua)
