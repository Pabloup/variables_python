# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print("{} es mayor que {}".format(texto_1, texto_2))
else:
    print("{} es mayor que {}".format(texto_2, texto_1))



# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print("la primera palabra es mas larga")
else:
    print("la segunda palabra es mas larga")

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
if texto_1[0] > texto_2[0]:
    print("la primera letra de la primera palabla es mayor a la de la segunda")
else:
    print("la primera letra de la segunda palabra es mayor a la de la primera")

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1:
    print("la primea palabra es igual a la copia")
else:
    print("la primera palabra no es igual a la copia")
# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if copia_texto_1 != texto_2:
    print("la copia no es igual a la segunda palabra")
else:
    print("la copia es igual a la segunda palabra")
