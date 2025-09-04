'''
variables se escriben en minusculas y si tienen 
mas de una palabra se separan con guion bajo _
'''

mi_variable = "Hola Mundo"
print(mi_variable)

variable_dos = 1234
print(variable_dos)

variable_tres = 12.34
print(variable_tres)

print()

#concatenar variables en un solo print
print(mi_variable, variable_dos, variable_tres) # imprime todas las variables en una sola linea
'''
la coma (,) en el print sirve para separar los 
diferentes elementos que se quieren imprimir
'''
print()
print(len(mi_variable)) # len() sirve para contar los caracteres de una variable

print()
#variables en una sola linea
nombre, apellido, age, alias = "Jose", "Hernandez", 27, "Techno"
print("mi nombre es:", nombre, apellido, "tengo", age, "años y mi alias es:", alias)

#inputs
nombre = input("Cual es tu nombre?: ")
apellido = input("Cual es tu apellido?: ")
age = input("Cual es tu edad?: ")
alias = input("Cual es tu alias?: ")
print("mi nombre es:", nombre, apellido, "tengo", age, "años y mi alias es:", alias)