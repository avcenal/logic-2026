"""* EJERCICIO:
* Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
* implemente una superclase Animal y un par de subclases Perro y Gato, junto con una función que sirva para imprimir el sonido que emite cada Animal."""
class Animal():
    def __init__(self):
        pass

    def sonido(self):
        print("MEH")

    def descripcion(self):
        print("Soy un animal")

class Perro(Animal):
    def __init__(self):
        pass

    def sonido(self):
        print("guau")

class Gato(Animal):
    def __init__(self):
        pass

    def sonido(self):
        print("miau")

my_dog = Perro()
my_dog.sonido()
my_dog.descripcion()

my_cat = Gato()
my_cat.sonido()

#las clases de Perro y Gato pueden sobreescribir métodos de la clase Animal, crear nuevos métodos
#Y utilizar también los de la clase Animal

for animal in [Perro(),Gato()]:
    animal.sonido()

#en este for se llama de manera genérica a cada elemento como un Animal.
#Python resuelve en ejecución qué sonido es el que tiene que aplicar, el de Perro o el de Gato.

"""* DIFICULTAD EXTRA (opcional):
* Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
* pueden ser Gerentes, Gerentes de Proyectos o Programadores.
* Cada empleado tiene un identificador y un nombre.
* Dependiendo de su labor, / tienen propiedades y funciones exclusivas
* actividad, y almacenan los empleados a su cargo."""