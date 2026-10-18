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
        return self.__stack.pop()

    def top(self):
        return self.__stack[len(self.__stack)-1]

class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        return self.__queue.pop(0)

    def front(self):
        return self.__queue[0]

my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(6)
print(my_stack.pop_stack())
print(my_stack.top())
print(my_stack)

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