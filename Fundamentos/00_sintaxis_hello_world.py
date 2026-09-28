"""
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
"""
#https://python.org

#comentario en una línea
"""
Comentarios
en varias
líneas
"""
'''
Esto también es
un comentario
en varias líneas
'''

my_variable = "esto es una variable"
#Python no tiene constantes, pero por convención:
MY_CONSTANT = "Mi constante" #pero se puede modificar el valor.

one_integer:int = 42
one_string:str = "esto es un string"
one_float: float = 7.5
one_boolean = True

print("Hola, Python!!")