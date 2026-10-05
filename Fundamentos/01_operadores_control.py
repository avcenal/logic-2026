"""
* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
#Aritméticos
print(3 + 4)
print("hola" + "Python")
print(5 - 2)
print(7 * 4)
print(9 / 3)
print(5 % 2)
print(3 ** 2)
print(10 // 3)

#Comparativos
print(3 > 4)
print(3 < 4)
print(3 == 4)
print(3 == 3)
print(3 >= 4)
print(3 <= 4)
print(3 != 4)

#Lógicos
print(3 > 4 and 3 == 3)
print(3 <= 4 or 3 > 4)
print(not(3 > 4))

#Condicionales
if 3 > 4:
    print("3 es mayor que 4")
elif 3 < 4:
    print("3 es menor que 4")
else:
    print("3 es igual a 4")


while True:
    try:
        user_number = int(input("Dime un número entero: "))
    except ValueError as error:
        print(f"tu opción no es un número entero: {error}")
    else:
        break
        
if user_number > 5:
    print(f"tu número {user_number} es mayor que cinco")
elif user_number == 5:
    print(f"Tu número es 5")
else:
    print(f"Tu número {user_number} es menor que 5")

#DIFICULTAD EXTRA
for number in range(10,56):
    if number != 16 and number % 3 != 0 and number % 2 == 0 or number == 55:
        print (number)