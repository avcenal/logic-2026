"""
* EJERCICIO:
* Implementa los mecanismos de introducción y recuperación de elementos propios de las
* pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
* o lista (dependiendo de las posibilidades de tu lenguaje).
"""
class EmptyStack(Exception):
    pass

class EmptyQueue(Exception):
    pass

class Stack:
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.__stack.append(item)

    def pop_stack(self):
        if self.is_empty():
            raise EmptyStack("La pila está vacía.")
        return self.__stack.pop()
        

    def top(self):
        if self.is_empty():
            raise EmptyStack("La pila está vacía.")
        return self.__stack[-1]

class Queue:
    def __init__(self):
        self.__queue = []

    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False
    
    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue("La cola está vacía.")
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            raise EmptyQueue("La cola está vacía.")
        return self.__queue[0]

my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(6)
print(my_stack.pop_stack())
print(my_stack.top())

#other_stack = Stack() #descomentar estas líneas para provocar EmptyStack
#print(other_stack.pop_stack())

my_queue = Queue()
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(8)
print(my_queue.front())
print(my_queue.dequeue())
print(my_queue.front())

#other_queue = Queue() #descomentar estas líneas para provocar EmptyQueue
#print(other_queue.dequeue())
"""
* DIFICULTAD EXTRA 1 (opcional):
*- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
* que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante","atrás" desencadenan esta acción, el resto se interpreta el nombre de una nueva web.
"""
from time import sleep
import re

def check_url(pattern, url) -> int: #evalúa si se cumple el patrón de URL definido. Devuelve 0 en caso de que no se cumpla
    return len(re.findall(pattern,url))


navigation_pattern = r"^((?:adelante|atr[á|a]s)+[\s]*(?!adelante|atr[á|a]s)+(.+))$"
url_pattern = r"(?:https:\/\/|http:\/\/){0,1}(?:www\.){0,1}[a-zA-Z-_0-9]+(?:\.[a-zA-Z0-9-_]+)(?:\.net|com|es|co|mx){0,1}"
#print(re.findall(navigation_pattern," www.test.com")[0][1])
web_browser = Stack()
option = ""
print("###################################################")
print("Te doy la bienvenida al navegador de avcenal.dev\n\nEscribe \"salir\" si quieres terminar el programa")
while "salir" not in option:
    if web_browser.is_empty():
        print("iniciando...")
        sleep(1)
        option = "adelante"
        option += input("introduce la primera web a la que quieres navegar: ").lower()
        if "atras" in option or "atrás" in option:
            print("No hay ninguna URL almacenada en el historial.")
        elif "salir" not in option:
            if check_url(url_pattern,re.findall(navigation_pattern, option)[0][1]) != 0:
                web_browser.push(re.findall(navigation_pattern, option)[0][1])
                print(f"Genial, ahora te encuentras en {web_browser.top()}")
            else:
                print("La URL no es válida")
    else:
        option = input("escribe \"adelante\" o \"atrás\" seguido de la web que quieres visitar: ").lower()
        if "adelante" in option:
            try:
                if check_url(url_pattern,re.findall(navigation_pattern, option)[0][1]) != 0:
                    web_browser.push(re.findall(navigation_pattern, option)[0][1])
                    print(f"Genial, ahora te encuentras en {web_browser.top()}")
                else:
                    print("La URL no es válida")
            except EmptyStack:
                print("No hay historial en el navegador.")
        elif "atrás" in option or "atras" in option:
            try:
                web_browser.pop_stack()
                print(f"Genial, ahora te encuentras en {web_browser.top()}")
            except EmptyStack:
                print("No hay historial en el navegador.")
        else:
            print("Tu opción no es válida, ")

"""
DIFICULTAD EXTRA 2
*- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de archivo.
"""
my_printer = Queue()
printer_input = ""
print("###################################################")
print("Te doy la bienvenida al sistema de impresión de avcenal.dev\n\nInstrucciones:\n- Para enviar un archivo a la cola de impresión basta con que escribas su nombre.\n- Al escribir \"imprimir\" se imprimirá el primer documento en la cola de impresión.\n- Para salir escribe simplemente \"salir\"\n")
while printer_input != "salir":
    printer_input = input("¿Qué deseas hacer?: ").lower()
    if "imprimir" in printer_input:
        try:
            print(f"Imprimiendo el archivo {my_printer.dequeue()}")
        except EmptyQueue:
            print("La cola de impresión está vacía")
    else:
        print(f"Guardando en la cola de impresión el archivo {printer_input}")
        my_printer.enqueue(printer_input)