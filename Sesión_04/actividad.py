"""
Requisitos:

- Dentro de una empresa se va a solicitar pedir nombre y apellido del empleado (input)
- Distrito de residencia y su sueldo actual (inputs)
- Sueldo y calculo del bono final del año, que será el triple del sueldo mensual menos el 10% del sueldo
- Todos estos datos van a ingresar en un diccionario
- Asignar a 3 variables usando asignación múltiple los valores del diccionario
- Mostrar por la terminal el mensaje de: "'Nombre' 'apellido', recibirá 'bono' soles de bono de fin de año"
"""
#Solicito nombre y apellido
nombre = input("Bienbenido a la empresa Claro, por favor ingrese su nombre: ")
apellido = input("A continuación ingrese su apellido: ")
#Solicito residencia y sueldo acutal
distrito = input("¿Cuál es su distrito de precedencia? ")
sueldo = input("¿Cuánto es su sueldo actual? ")
#Sueldo y calculo del bono final
sueldo = float(sueldo)
bono_final = (sueldo * 3) - (sueldo * 0.1)
#Diccionario
usuario = {}
usuario["nombre"] = nombre
usuario["apellido"] = apellido
usuario["distrito"] = distrito
usuario["sueldo"] = sueldo
usuario["bono_final"] = bono_final
#Asiganación multiple
empleado, remuneración, abono = nombre, sueldo, bono_final
#Print
print("{} {}, recibirá {} soles de bono de fin de año".format(empleado, apellido, abono))
print(usuario)


