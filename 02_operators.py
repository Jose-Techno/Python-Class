# Operadores #

# Aritméticos
print
'''
se usan para realizar operaciones matemáticas
como suma, resta, multiplicación, división, etc.
'''
print()

suma = 5 + 3          # Suma
print("Suma: ", suma)
resta = 5 - 3         # Resta
print("Resta: ", resta)
multiplicacion = 5 * 3 # Multiplicación
print("Multiplicación: ", multiplicacion)
division = 5 / 3      # División
print("División: ", division)
modulo = 5 % 3        # Módulo = resto de la división
print("Módulo: ", modulo)
exponente = 5 ** 3    # Exponente
print("Exponente: ", exponente)
floor_division = 5 // 3 # División entera = redondea hacia abajo
print("División entera: ", floor_division)  
print()

# Operadores usados en cadenas de texto
print("operadores en cadenas de texto")
'''
se usan para manipular cadenas de texto
'''
print()

print("Hola " + "Mundo") # Concatenación de cadenas
print("Hola " * 3)       # Repetición de cadenas
print()

# Operadores de Comparación
print
'''
se usan para comparar valores y devuelven
un valor booleano (True o False)
'''
print()

a = 5
b = 3
print(a == b)  # Igualdad
print(a != b)  # Desigualdad
print(a > b)   # Mayor que
print(a < b)   # Menor que
print(a >= b)  # Mayor o igual que
print(a <= b)  # Menor o igual que
print()


#operadores de comparación en cadenas de texto
print("operadores de comparación en cadenas de texto")
'''
Comparación de cadenas de texto que se basa en el orden lexicográfico
(como en un diccionario) y en el valor Unicode de los caracteres.
lexicográfico significa que las cadenas se comparan carácter por carácter
de izquierda a derecha, utilizando el valor Unicode de cada carácter.
'''
print()

c = "Hola"
d = "Mundo"
print(c == d)  # Igualdad
print(c != d)  # Desigualdad
print(c > d)   # Mayor que (comparación lexicográfica)
print(c < d)   # Menor que (comparación lexicográfica)
print(c >= d)  # Mayor o igual que (comparación lexicográfica)
print(c <= d)  # Menor o igual que (comparación lexicográfica)
print()

# Operadores Lógicos#
print("Operadores Lógicos")
'''
se usan para combinar expresiones booleanas
y devuelven un valor booleano (True o False)
'''
print()

x = True
y = False
print(x and y)  # AND lógico
print(x or y)   # OR lógico
print(not x)    # NOT lógico   
print(not y)    # NOT lógico
print((5 > 3) and (2 < 4))  # Combinación de expresiones booleanas
print((5 > 3) or (2 > 4))   # Combinación de expresiones booleanas
print(not (5 > 3))          # Negación de una expresión booleana            
print(not (2 > 4))          # Negación de una expresión booleana
print((5 > 3) and (2 > 4) or (3 == 3)) # Combinación de múltiples expresiones booleanas
print((5 > 3) or (2 > 4) and (3 == 3)) # Combinación de múltiples expresiones booleanas
print(not (5 > 3) and (2 < 4) or (3 == 3)) # Combinación de múltiples expresiones booleanas
print(not (5 > 3) or (2 < 4) and (3 == 3)) # Combinación de múltiples expresiones booleanas
print((5 > 3) and not (2 < 4) or (3 == 3)) # Combinación de múltiples expresiones booleanas
print((5 > 3) or not (2 < 4) and (3 == 3)) # Combinación de múltiples expresiones booleanas
print((5 > 3) and (2 < 4) and (3 == 3)) # Combinación de múltiples expresiones booleanas
print((5 > 3) or (2 < 4) or (3 == 3)) # Combinación de múltiples expresiones booleanas
print(not (5 > 3) and not (2 < 4) or not (3 == 3)) # Combinación de múltiples expresiones booleanas
print(not (5 > 3) or not (2 < 4) and not (3 == 3)) # Combinación de múltiples expresiones booleanas
print((5 > 3) and not (2 < 4) or not (3 == 3)) # Combinación de múltiples expresiones booleanas
print((5 > 3) or not (2 < 4) and not (3 == 3)) # Combinación de múltiples expresiones booleanas             
print()

# Operadores de Asignación #
print("Operadores de Asignación")
'''
se usan para asignar valores a variables
''' 
print()

e = 5       # Asignación simple
print("Valor inicial de e: ", e)
e += 3      # Suma y asignación
print("Después de e += 3: ", e)
e -= 2      # Resta y asignación
print("Después de e -= 2: ", e)
e *= 4      # Multiplicación y asignación
print("Después de e *= 4: ", e)
e /= 2      # División y asignación
print("Después de e /= 2: ", e)
e %= 3      # Módulo y asignación
print("Después de e %= 3: ", e)
e **= 2     # Exponente y asignación
print("Después de e **= 2: ", e)
e //= 2     # División entera y asignación
print("Después de e //= 2: ", e)    

