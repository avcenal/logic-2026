"""/*
* EJERCICIO:
* Entiende el concepto
de recursividad creando una función recursiva que imprima
* números del
100 al 0.
"""
def recursion_numbers(number: int = 100):
    print(number)
    if number != 0:
        recursion_numbers(number - 1)

recursion_numbers()

"""
* DIFICULTAD EXTRA (opcional):
≥
* Utiliza el concepto de recursividad para:
* - Calcular el factorial de un número concreto (la función recibe ese número).
* - Calcular el valor de un elemento concreto (según su posición) en la
* sucesión de Fibonacci (la función recibe la posición).
*/
"""
def factorial(number : int|float):
    if number == 1 or number == 0:
        return number
    else:
        return number * factorial(number - 1)

print(factorial(3))
print(factorial(7))

def fibonacci_position(position:int):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci_position(position - 1) + fibonacci_position(position -2)

print(fibonacci_position(4))
print(fibonacci_position(8))


