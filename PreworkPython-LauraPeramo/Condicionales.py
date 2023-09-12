"""1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos."""

x = -5
if x < 0:
  print("El número es Negativo")
else:
  print("El número es positivo")

if x % 2 == 0:
  print("El número es par")
else:
  print("El número es impar")
  
numeros = [7, 65, 12]

mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
      mayor = numero
print("Mayor", mayor)