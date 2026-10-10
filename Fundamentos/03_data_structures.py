"""
* EJERCICIO:
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
*- Utiliza operaciones de inserción, borrado, actualización y ordenación.
*
"""
#LISTAS
my_list = ["Alex", "Valderrama", 42]
my_list.append(1.82) #añade al final 1.82
print(my_list)
my_list.insert(2, "Cenalmor") #inserta en el index 2
print(my_list)
my_list.pop(2) #borra lo contenido en el index 2
print(my_list)
my_list.insert(2, "Valderrama") #inserta de nuevo Valderrama en la versión 2
print(my_list)
my_list.remove("Valderrama") #y borra la primera ocurrencia de Valderrama
print(my_list)
other_list = [3, 6, 2, 8, 1]
other_list.sort() #ordena de menor a mayor
print(other_list)
other_list.sort(reverse= True) #ordena de mayor a menor
print(other_list)

#TUPLAS: al ser una estructura inmutable no tiene ninguna acción para modificarla. Habria que pasarla a lista y después a tupla de nuevo para modificarla
my_tuple = ("Alex","Valderrama", "Alex")
print(my_tuple.count("Alex"))
print(my_tuple.index("Valderrama"))

#SETS: conjunto de datos no ordenado
my_set = {"Alex", "Valderrama", 42}
my_set.add(1.82) #se añade el nuevo valor
print(my_set)
my_set.add("Alex") #como es un valor duplicado no se añade
print(my_set)
my_set.remove(1.82) #elimina el elemento del set
print(my_set)
my_set_value = my_set.pop() #se elimina un elemento del set y se guarda en una variable
print(my_set)
print(my_set_value)
my_set.update([42, 1.82, "Alex"]) #se puede actualizar el set con un iterable, en el ejemplo, una lista. Se añaden sus valores (los no repetidos)
print(my_set)

#DICCIONARIOS
my_dict = {
    "first_name": "Alex",
    "last_name": "Valderrama",
    "age": 42,
    "heigh": 1.82,
    "programming_languages": ["Python", "Javascript"]
}

my_dict["status"] = "married" #añade "status" como una clave más del diccionario con su valor
print(my_dict)
my_dict.pop("status") #borra un par clave/valor dada su clave
print(my_dict)
my_dict.update({"age":"43"}) #update actualiza el diccionario con un nuevo par clave valor. Si la clave existe actualiza el valor
print(my_dict)
my_dict.update({"age":"43", "status": "married"}) #si una clave no existe, la añade
print(my_dict)
my_dict_value = my_dict.popitem() #elimina el último par clave valor y se almacena en una tupla
print(my_dict_value)

"""
* DIFICULTAD EXTRA (opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
* los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
* (o el número de dígitos que quieras)
* - También se debe proponer una operación de finalización del programa.
"""
class Contact:
    def __init__(self, name:str, phone:str):
        self.details = {
            "name": name,
            "phone": phone            
        }

    def print_contact(self):
        print(f"- Nombre: {self.details["name"]}\n- Teléfono: {self.details["phone"]}")

class Agenda:
    def __init__(self):
        self.__contacts = []

    def include_contact(self, contact: Contact):
        self.__contacts.append(contact)

    def print_agenda(self):
        for element in self.__contacts:
            element.print_contact()

name = "Alex"
phone = "+32123456789"
one_contact = Contact(name, phone)
my_agenda = Agenda()
my_agenda.include_contact(one_contact)
my_agenda.print_agenda()
