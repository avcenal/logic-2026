"""
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
    * posibilidades del plenguaje:
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
Debes hacer print por consola del resultado de todos los ejemplos.
tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
DIFICULTAD EXTRA (opcional):
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
* Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""
#SIN PARÁMETROS
def print_hello_python():
    print("Hello, Python!")

print_hello_python()

#SIN RETORNO
def print_sum_two_values(value_one:int, value_two:int):
    sum = value_one + value_two
    print(sum)

print_sum_two_values(7, 8) #solo se muestra el resultado en terminal pero no se puede reutilizar

#CON UN PARÁMETRO DE RETORNO
def sum_two_values(value_one:int, value_two:int):
    return value_one + value_two

one_sum = sum_two_values(6, 2) #en este caso si se puede reutilizar el valor de la suma de los valores
print(one_sum)

#CON VARIOS PARÁMETROS DE RETORNO
def sum_and_rest_two_values(value_one:int, value_two:int):
    return value_one + value_two, value_one - value_two

sum, rest = sum_and_rest_two_values (4, 3)
print(sum)
print(rest)

# FUNCIÓN DENTRO DE OTRA FUNCIÓN
def list_values(one_float_list:list):
    def convert_to_integer(one_float:float): #esta función solo trabaja con sus valores locales
        return int(one_float)
    return [convert_to_integer(value) for value in one_float_list]

print(list_values([2.0, 5.4, 1.8, 9.0]))

# CLOSURE
def function_one(one_value:int):
    def function_two(value_one:int, value_two:int):
        return value_one + value_two - one_value
    return function_two

print(function_one(5)(2, 6))

#HIGH LEVEL FUNCTIONS
one_list = [7, 8, 4, 6, 1]
map_list = list(map(lambda x : x * 5, one_list))
print(map_list)
filter_list = list(filter(lambda x : x > 5, one_list))
print(filter_list)

from functools import reduce
reduced_values = reduce(lambda x, y : x - y, one_list)
print(reduced_values)

#DIFICULTAD EXTRA
def function_extra(text_one: str, text_two:str) -> int:
    counter = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_one+text_two)
        elif number % 3 == 0:
            print(text_one)
        elif number % 5 == 0:
            print(text_two)
        else:
            counter += 1
            print(number)
    return counter

print(f"los números se han impreso {function_extra("Alex", "Sole")} veces")