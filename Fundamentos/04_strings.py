"""
*EJERCICIO:
* Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
* en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
* - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
interpolación, verificación..
"""
my_string = "hello, Python"
#funciones built-in
print(my_string.title())
print(my_string.capitalize())
print(my_string.upper())
print(my_string.lower())
print(my_string.count("o"))
print(my_string.encode())
print(my_string.startswith("h"))
print(my_string.endswith("o"))
print(my_string.find("t"))
print(my_string.isnumeric())
print(len(my_string))

#substrings, slices y reverse
print(my_string[2:9]) #substring desde la posición 2 hasta la 8
print(my_string[-1]) #imrpime el primer caracter desde el final
print(my_string[-5]) #imprime el quinto caracter desde el final
print(my_string[::-1]) #imprime al revés
print(my_string[::-5]) #imprime cada 4 caracteres al revés

#interpolación: tres formas
name = "Alex"
age = 42
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))
print("My name is %s and I am %d years old" %(name, age))

#operaciones
other_string = "Python"
print(other_string, my_string)
print(other_string + my_string)
print(other_string * 2)
print(other_string * 2)

#caracteres especiales
print("Hello\nPython")
print("Hello\tPython")

"""
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
"""
