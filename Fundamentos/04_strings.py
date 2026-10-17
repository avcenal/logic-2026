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
def is_palindrome(word:str):
    return(word.lower() == word[::-1].lower())

def letters_in_set(word:str):
    letters_set = set()
    for letter in word:
        letters_set.add(letter)
    return letters_set
    
def are_anagrams(word_one: str, word_two: str):
    if len(word_one) == len(word_two):
        word_one_letters = letters_in_set(word_one.lower())
        word_two_letters = letters_in_set(word_two.lower())
        if (len(word_one_letters.difference(word_two_letters))==0):
            return True
        else:
            return False
    else:
        return False

def is_isogram(word: str):
    word = word.lower()
    limit = word.count(word[0])
    for letter in word[1::]:
        if word.count(letter) != limit:
            return False
    return True

def check_words(word_one:str, word_two:str):
    summary = ""
    if is_palindrome(word_one) and is_palindrome(word_two):
        summary = f"{word_one} y {word_two} son palíndromos\n"
    elif not is_palindrome(word_one) and is_palindrome(word_two):
        summary = f"{word_one} no es un palíndromo y {word_two} si lo es\n"
    elif is_palindrome(word_one) and not is_palindrome(word_two):
            summary = f"{word_one} es un palíndromo y {word_two} no lo es\n"
    else:
        summary = f"Ni {word_one} ni {word_two} son palíndromos\n"

    if are_anagrams(word_one,word_two):
        summary += "Si son anagramas\n"
    else:
        summary += "No son anagramas\n"

    if is_isogram(word_one) and is_isogram(word_two):
        summary += f"{word_one} y {word_two} son isogramas"
    elif not is_isogram(word_one) and is_isogram(word_two):
        summary += f"{word_one} no es un isograma y {word_two} si lo es"
    elif is_isogram(word_one) and not is_isogram(word_two):
        summary += f"{word_one} es un isograma y {word_two} no lo es"
    else:
        summary += f"Ni {word_one} ni {word_two} son isogramas"

    print(summary)

check_words("Oso", "oso")
check_words("arroz", "rozar")
check_words("pelo", "gato")
check_words("anona", "AnonA")
check_words("perla", "Paler")