"""
EJERCICIO:
* Explora el concepto de manejo de excepciones según tu lenguaje.
* Fuerza un error en tu código, captura el error, imprime dicho error
* y evita que el programa se detenga de manera inesperada.
* Prueba a dividir "10/0" o acceder a un índice no existente
* de un listado para intentar provocar un error.
"""
my_int = 5
try:
    result = my_int / 0
except ZeroDivisionError as error:
    print(f"Has tratado de dividir {my_int} por cero: {error}")

my_list = [1, 3, 6, 8, 11]
try:
    print(my_list[5])
except IndexError as error:
    print(f"Parece que estás tratando de acceder a un elemento que no existe en la lista: {error}")
else:
    print("¡Finalizado!")
finally:
    print("Terminando el programa")

my_dict = {
    "name": "Alex",
    "last_name": "Valderrama",
    "age": 42,
}
try:
    print(my_dict["first_name"])
except KeyError as error:
    print(f"Ups, parece que estás tratando de acceder a un item inexistente en el diccionario: {error}")

try:
    print("5" + 2)
except TypeError as error:
    print(f"Los tipos de dato con incompatibles: {error}")

try:
    my_int.reverse()
except AttributeError as error:
    print(f"Parece que \"my_int\" al ser integer no tiene función \"reverse\"")

"""my_other_int = 0
if my_other_int == 0:
    raise ZeroDivisionError ("Cudidado, \"my_other_int\" es cero")"""

"""
* DIFICULTAD EXTRA (opcional):
* Crea una función que sea capaz de procesar parámetros, pero que también
* pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
* corresponderse con un tipo de excepción creada por nosotros de manera
* personalizada, y debe ser lanzada de manera manual) en caso de error.
* - Captura todas las excepciones desde el lugar donde llamas a la función.
* - Imprime el tipo de error.
* - Imprime si no se ha producido ningún error.
* - Imprime que la ejecución ha finalizado
"""
class SecondIntegerIsZeroOrNegative(Exception):
    def __init__(self, message: str = "Como segundo número debes elegir un número mayor que cero."):
        super().__init__(message)

def my_function():
    while True:
        try:
            first_int = int(input("Introduce el primer número: "))
        except ValueError as error:
            print("debes elegir un número")
        else:
            try:
                second_int = int(input("Introduce el segundo número: "))
            except ValueError as error:
                        print("debes elegir un número")
            else:
                if (second_int <= 0):
                    raise SecondIntegerIsZeroOrNegative
                else:
                    print(first_int / second_int)
                    print("no se ha prodducido ningún error")
            finally:
                print("La ejecución ha finalizado") #realmente el bloque finally solo se ejecutará si no llega al raise
            break

my_function()