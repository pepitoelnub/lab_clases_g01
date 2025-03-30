"""
Requisitos

1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string (solamente caracteres), 1 variable string
con contenido solamente numérico y 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica
(realizar conversiones si es necesario)
3. Obtener y mostar la suma de las 2 variables enteras más la variable string numérica y la
variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostarar el resultado entero o la parte entera de las 2 variables int: //
6. Obtener una pontencia usando una de las variables flotantes como base y la variable entera como potencia
"""

ent_01 = 70
ent_02 = 55
float_01 = 14.3
float_02 = 10.4
var_1 = "Hola"
var_2 = "400"
var_bool = True

#Suma de una variable entera y variable string numerica
suma_01 = ent_01 + int(var_2)
print("suma_01: {}".format(suma_01))

#Suma de las 2 variables enteras, más la variable string numérica y la variable flotante
suma_02 = ent_01 + ent_02 + int(var_2) + float_01
print("suma_02: {}".format(suma_02))

#módulo de las variables enteras
módulo_01 = ent_01 % ent_02
print("módulo_01: {}".format(módulo_01))

#mostrar el resultado entero o la parte entera de las variables int
división_01 = ent_01 // ent_02
print(f"división entera: {int( división_01)}")

#Obtener potencia con variable flotante y entera
potencia_01 = float_01 ** ent_02
print("potencia_01: {}".format(potencia_01))


