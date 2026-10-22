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
* DIFICULTAD EXTRA (opcional):
*- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
* que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante","atrás" desencadenan esta acción, el resto se interpreta el nombre de una nueva web.
*- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de
"""
from time import sleep
import re
navigation_pattern = r"^((?:adelante|atr[á|a]s)+[\s]*(?!adelante|atr[á|a]s)+(.+))$"
#print(re.findall(navigation_pattern," www.test.com")[0][1])
web_browser = Stack()
option = ""
print("###################################################")
print("Te doy la bienvenida al navegador de avcenal.dev\n\nEscribe \"salir\" si quieres terminar el programa")
while "salir" not in option:
    if web_browser.is_empty():
        print("iniciando...")
        sleep(1)
        option = "adelante "
        option += input("introduce la primera web a la que quieres navegar: ")
        if "salir" not in option:
            web_browser.push(re.findall(navigation_pattern, option)[0][1])
            print(f"Genial, ahora te encuentras en {web_browser.top()}")
    else:
        option = input("escribe \"adelante\" o \"atrás\" seguido de la web que quieres visitar: ")
        if "adelante" in option:
            try:
                web_browser.push(re.findall(navigation_pattern, option)[0][1])
                print(f"Genial, ahora te encuentras en {web_browser.top()}")
            except EmptyStack:
                print("No hay historial en el navegador.")
        elif "atrás" in option:
            try:
                web_browser.pop_stack()
                print(f"Genial, ahora te encuentras en {web_browser.top()}")
            except EmptyStack:
                print("No hay historial en el navegador.")
        else:
            print("Tu opción no es válida, ")

