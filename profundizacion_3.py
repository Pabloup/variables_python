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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print("en este ejercicio veremos estimaciones con temperaturas")
print("ingrese 3 valores de temperatura a pedido del sistemas")
print("ingrese el primer valor de temperatura")

valor_1 = int(input())
print("ingrese el segundo valor de temperatura")
valor_2 = int(input())
print("ingrese el tercero")
valor_3 = int(input())

if valor_1 > (valor_2 and valor_3):
    print("el primer valor es el mas alto")
elif valor_2 > (valor_1 and valor_3):
    print("el segundo valor es el mas alto")
else:
    print("el tercer valor es el mas alto")

if valor_1 < (valor_2 and valor_3):
    print("el primer valor es la temperatura mas baja")
elif valor_2 < (valor_1 and valor_3):
    print("el segundo valor es la temperatura mas baja")
else:
    print("el tercer valor es la temperatura mas baja")

print("el promedio de las temperaturas ingresadas es de" , (valor_1 + valor_2 + valor_3) / 3)