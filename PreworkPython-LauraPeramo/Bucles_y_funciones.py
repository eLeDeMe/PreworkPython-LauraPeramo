# Ejercicio 1

def es_par(numero):
    return numero % 2 == 0


num = int(input("Ingresa un número: "))
if es_par(num):
    print("Es un número par.")
else:
    print("Es un número impar.")

# Ejercicio 2


def factorial(numero):
    resultado = 1
    for i in range(1, 5 + 1):
        resultado *= i
    return resultado
    num = int(input("Ingresa un número: "))


print("El factorial de", 6, "es:", factorial(6))

# Ejercicio 3


def contar_digitos(numero):
    return len(str(numero))


num = int(input("Ingresa un número: "))

print("La cantidad de dígitos es:", contar_digitos(num))

# Ejercicio 4


def encontrar_maximo(lista):
    maximo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo


numeros = [10, 3, 75, 12]

print("El número máximo es:", encontrar_maximo(numeros))

# Ejercicio 5 #


def sumar_digitos(numero):
    Suma = 0

    while numero > 0:
        Suma += numero % 10
        numero //= 10
    return Suma


num = int(input("Ingresa un número: "))

print("La suma de los digitos es:", sumar_digitos(num))

# Ejercicio 6#


def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        maximo = max(a, b)
    while True:
        if maximo % a == 0 and maximo % b == 0:
            return maximo
        maximo += 1


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("El MCM es:", mcm(num1, num2))

# Ejercicio 7#


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

print("El área del triángulo es:", calcular_area_triangulo(base, altura))


def verificar_signo(num):
    if num > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    else:
        return "cero"


num = float(input("Ingresa un número: "))
print("El número es:", verificar_signo(num))


def contar_letras(palabra):
    contador = 0
    for letra in palabra:
        if letra.isalpha():
            contador += 1
    return contador


palabra = input("Ingresa una palabra: ")

print("La cantidadde letras es:", contar_letras(palabra))

# Ejercicio 8#


def valor_absoluto(lista):
    for i in range(len(lista)):
        lista[i] = abs(lista[i])
    return lista


numeros = [5, -12, 3, -8, 9]
print("Lista con valores absolutos:", valor_absoluto(numeros))

# Ejercicio 9#


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False

        return True


num = int(input("Ingresa un número: "))
if es_primo(num):
    print("Es un número primo.")
else:
    print("No es un número primo.")

# Ejercicio 10#


def mcd(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("El MCD es:", mcd(num1, num2))
