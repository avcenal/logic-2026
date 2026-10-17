"""
EJERCICIO:
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
* - Muestra ejemplos de funciones COn variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada en el momento de ser modificadas.
* (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""
#paso de un parámetro POR VALOR: se realiza una copia local del parámetro dentro de una función y cualquier cambio
#no afectará al parámetro fuera de esa función

#en Python un número entero se considera siempre como si se pasara por valor
def multiply_ten(number:int|float):
    number *= 10

my_number = 10
multiply_ten(my_number)
print(my_number)

#e igual con los float
my_float_number = 4.5
multiply_ten(my_float_number)
print(my_float_number)

#Y también ocurre con los strings
def add_surname(name: str):
    name += " Valderrrama"

my_name = "Alex"
add_surname(my_name)
print(my_name)

#en cambio en Python una lista se considera siempre como si se pasara por referencia.
#PASO POR REFERENCIA: se altera el parámetro original dentro y fuera de la función, se apunta al mismo espacio en memoria.

def append_number(integer_list: list):
    integer_list.append(20)
    print(id(integer_list))

my_list = [1, 5, 7, 9]
print(id(my_list))
append_number(my_list)
print(my_list)

#ocurre lo mismo con los diccionarios
def add_parameter_to_dict (one_dict: dict):
    one_dict["age"] = 42

my_dict = {
    "name": "Alex",
    "last_name": "Valderrama"
}

add_parameter_to_dict(my_dict)
print(my_dict)

#e igual ocurre con los sets
def add_parameter_to_set(one_set: set):
    one_set.add(42)

my_set = {"Alex", "Valderrama"}
add_parameter_to_set(my_set)

print(my_set)

#incluso fuera de funciones, por ejemplo, con listas:
one_list = my_list
print(my_list)
print(one_list)
my_list.append(30)
print(my_list)
print(one_list)
one_list.append(40)
print(my_list)
print(one_list)

#Conclusión: cualquier estructura de datos más allá de los tipos de datos básicos, Python considera que se pasa por referencia
#es decir, trabaja con la misma posición de memoria de dicho parámetro.
#en cambio, para los tipos de datos básicos, crea una copia en memoria y no altera el parámetro original.
#nota: es posible usar la función "id()" para ver el espacio en memoria con le que se trabaja tanto fuera como dentro de la función
#esto está hecho en la función que modifica la lista.

#para los tipos de datos básicos, se ha de utilizar return, un ejemplo con el integer. Apuntan al mismo espacio en memoria
def multiply_ten_correctly(number: int|float):
    print(id(number))
    return number * 10

my_other_integer = 5
print(id(my_other_integer))
print(multiply_ten_correctly(my_other_integer))

"""
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
    Estos parametros los intercambia entre ellos en su interior, los retorna, y su retorno
    se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
    variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
    Comprueba también que se ha conservado el valor original en las primeras.
"""