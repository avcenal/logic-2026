"""
* EJERCICIO:
* Implementa los mecanismos de introducción y recuperación de elementos propios de las
* pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
* o lista (dependiendo de las posibilidades de tu lenguaje).
"""
class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop_stack(self):
        try:
            return self.__stack.pop()
        except IndexError as error:
            print(f"La pila está vacía. Error: {error}.")
        

    def top(self):
        try:
            return self.__stack[-1]
        except IndexError as error:
            print(f"La pila está vacía. Error: {error}.")

class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        try:
            return self.__queue.pop(0)
        except IndexError as error:
            print(f"La cola está vacía. Error: {error}.")

    def front(self):
        try:
            return self.__queue[0]
        except IndexError as error:
            print(f"La cola está vacía. Error: {error}.")

my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(6)
print(my_stack.pop_stack())
print(my_stack.top())

other_stack = Stack()
print(other_stack.pop_stack())

my_queue = Queue()
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(8)
print(my_queue.front())
print(my_queue.dequeue())
print(my_queue.front())
"""
* DIFICULTAD EXTRA (opcional):
*- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
* que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante",
"atrás" desencadenan esta acción, el resto se interpreta
el nombre de una nueva web.
*- Utilizando la implementación de cola y cadenas
de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de
"""