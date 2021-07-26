# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print("a continuacion ingrese 3 numeros y podra ver si cada uno es par o impar")
print("ingrese un numero")
numero_1 = int(input())
print("ingrese el segundo numero")
numero_2 = int(input())
print("ingrese el tercer numero")
numero_3 = int(input())

if (numero_1 % 2) == 0:
    print("el primer numero es par")
else:
    print("el primer numero es impar")

if (numero_2 % 2) == 0:
    print("el segundo numero es par")
else:
    print("el segundo numero es impar")

if (numero_3 % 2) == 0:
    print("el tercer numero es par")
else:
    print("el tercer numero es impar")

print("espero les haya servido, muchas gracias..!")