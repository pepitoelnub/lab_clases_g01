"""Listas en Python"""

"""
Requisitos:

- Crear dos lista de personas vacías
- Agregar los datos de nombre, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edad // por índice
- Sumar ambas listas y mostrar el resultado en la terminal
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas
- Mostrar la lista vacía de la segunda persona aplicando el método respectivamente

"""
persona_01 = []
persona_02 = []

persona_01.append("itzel")
persona_02.append("jhoshua")
persona_01.append(17)
persona_02.append(19)
persona_01.append("Genetista")
persona_02.append("Ingeniero")

suma_edades = persona_01[1] + persona_02[1]
print("La suma de las edades es: {}".format(suma_edades))

suma_de_listas = persona_01 + persona_02
print("La suma de las listas es: {}". format(suma_de_listas))

suma_de_listas.reverse()
print("La suma de la lista en reversa es: {}".format(suma_de_listas))

suma_de_listas.remove(19)
suma_de_listas.remove(17)

print(suma_de_listas)

persona_02.clear()
print("la lista 02 actualizada: ", persona_02)