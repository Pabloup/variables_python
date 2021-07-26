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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra)

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
print("ingrese 3 palabras a pedido del sistema, y seran ordenadas alfabeticamente")

print("ingrese la primera palabra")
palabra_1 = str(input())
print("ingrese la segunda palabra")
palabra_2 = str(input())
print("ingrese la tercer palabra")
palabra_3 = str(input())

if (palabra_1 > palabra_2) and (palabra_1 > palabra_3) and (palabra_2 > palabra_3):
    print("el orden es:" , palabra_1 , palabra_2 , palabra_3)

elif (palabra_1 > palabra_2) and (palabra_1 > palabra_3) and (palabra_3 > palabra_2):
    print("el orden es:" , palabra_2 , palabra_1 , palabra_3)

elif (palabra_2 > palabra_1) and (palabra_2 > palabra_3) and (palabra_1 > palabra_3):
    print("el orden es:" , palabra_2 , palabra_1 , palabra_3)

elif (palabra_2 > palabra_1) and (palabra_2 > palabra_3) and (palabra_3 > palabra_1):
    print("el orden es:" , palabra_2 , palabra_3 , palabra_1)

elif(palabra_3 > palabra_1) and (palabra_3 > palabra_2) and (palabra_1 > palabra_2):
    print("el orden es:" , palabra_3 , palabra_1 , palabra_2)

else:
    print("el orden es:" , palabra_3 , palabra_2 , palabra_1)



if len(palabra_1) > len(palabra_2) and len(palabra_1) > len(palabra_3) and len(palabra_2) > len(palabra_3):
    print("el orden es:" , palabra_1 , palabra_2 , palabra_3)

elif len(palabra_1) > len(palabra_2) and len(palabra_1) > len(palabra_3) and len(palabra_3) > len(palabra_2):
    print("el orden es:" , palabra_1 , palabra_3 , palabra_2)

elif len(palabra_2) > len(palabra_1) and len(palabra_2) > len(palabra_3) and len(palabra_1) > len(palabra_3):
    print("el orden es:" , palabra_2 , palabra_1 , palabra_3)

elif len(palabra_2) > len(palabra_1) and len(palabra_2) > len(palabra_3) and len(palabra_3) > len(palabra_1):
    print("el orden es:" , palabra_2 , palabra_3 , palabra_1)

elif len(palabra_3) > len(palabra_2) and len(palabra_3) > len(palabra_1) and len(palabra_1) > len(palabra_2):
    print("el orden es:" , palabra_3 , palabra_1 , palabra_2)

else:
    print("el orden es:" , palabra_3 , palabra_2 , palabra_1)
    


