"""
Requisitos

1. Crear variables para los valores de nombre, profesión y ciudad
2. Crear 2 variables para la remuneración de enero y febrero (más de 1000)
3. Crear 1 variable deonde se sumará el ingreso de los meses de enero y feberero
4. Mostrar en pantalla el mensaje de:

Mnesaje final:
"Hola soy 'nombre' mi 'profesión' y mi remuneración acumulada es de 'remuneración total'"

"""


nombre = "Itzel"
profesión = "Genetista"
ciudad = "Ica"

rem_enero = 1000
rem_febrero = 900
suma_rem = rem_enero + rem_febrero

print("Hola soy {} mi {} y mi remuneración acumulada es de {}.".format(nombre, profesión, suma_rem))

