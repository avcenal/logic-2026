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
from time import sleep
import re

class Contact:
    def __init__(self, name:str, phone:str):
        self.details = {
            "name": name,
            "phone": phone            
        }

    def print_contact(self):
        print(f"- Nombre: {self.details["name"]}\n- Teléfono: {self.details["phone"]}")

    def get_contact_name(self):
        return self.details["name"]

    def get_contact_phone(self):
        return self.details["phone"]

    def update_contact(self, contact: Contact):
        return self.details.update({"name":contact.get_contact_name(), "phone": contact.get_contact_phone()})

class Agenda:
    def __init__(self):
        self.__contacts = []

    def find_contact(self, name:str):
        return self.__contacts.index((list(filter(lambda x: x.get_contact_name() == name, self.__contacts)))[0])
    
    def add_new_contact(self, contact: Contact):
        self.__contacts.append(contact)

    def get_number_of_contacts(self):
        return len(self.__contacts)

    def show_contact(self, index:int):
        self.__contacts[index].print_contact()

    def delete_contact(self,name: str):
        __contact_index = self.find_contact(name)
        self.__contacts.pop(__contact_index)

    def update_contact(self,contact:Contact):
        __contact_index = self.find_contact(contact.get_contact_name())
        self.__contacts[__contact_index].update_contact(contact)

    def print_agenda(self):
        for index, element in enumerate(self.__contacts):
            print(f"Contacto {index+1}:")
            element.print_contact()
            print("\n")

def phone_checker(phone: str):
    PHONE_PATTERN = r"\+[0-9]{11}" #el patrón admite números con un "+" y el prefijo de país: +34123456789
    while len(re.findall(PHONE_PATTERN,phone)) == 0:
        phone = input("Parece que el teléfono no tiene un formato adecuado, prueba de nuevo: ")

    return phone

def contact_already_exist(agenda: Agenda, contact: Contact):
    try:
        agenda.find_contact(contact.get_contact_name())
    except:
        return False
    else:
        return True

def show_full_agenda(agenda: Agenda):
    if agenda.get_number_of_contacts() != 0:
        print(f"La agenda tiene un total de {agenda.get_number_of_contacts()} contactos")
        option = input("¿Quieres mostrarla completa? (S/N): ").upper()
        print("\n")
        match option:
            case "S":
                agenda.print_agenda()
            case "N":
                print("Ok, volvamos a las opciones anteriores\n")
    else:
        print("Esta agenda no tiene aún ningún contacto guardado...\n")

def add_new_contact(agenda: Agenda, contact: Contact):
    option = ""
    if contact_already_exist(agenda, contact): #si el contacto existe, lo actualizará
        print(f"El contacto de {contact.get_contact_name()} ya existe en la agenda:")
        option = input(f"¿quieres actualizarlo? (S/N): ").upper()
        while option != "N":
            match option:
                case "S":
                    update_contact(agenda, contact.get_contact_name(), contact.get_contact_phone())
                    break
                case "N":
                    break
                case _:
                    option = input(f"Tu opción no es válida, ¿quieres actualizar el contacto de {name}?(S/N): ")
                    print("\n")
    else:
        agenda.add_new_contact(contact) #si no existe lo crea

def find_contact(agenda: Agenda, name: str):
    try:
        index = agenda.find_contact(name)
        agenda.show_contact(index)
    except IndexError as e:
        print(f"El contacto no se encuentra en la agenda. Error: {e}")
    except:
        print(f"Ha ocurrido un error. Error: {e}")
    print("\n")

def update_contact(agenda: Agenda, name: str, phone: str = None):
    try:
        index = agenda.find_contact(name)
    except:
        option = input("El contacto no existe en la agenda, ¿Quieres añadirlo? (S/N): ").upper()
        while option != "N":
            match option:
                case "S": #se podría incluir código para dar a elegir actualizar el nombre o el teléfono
                    if phone == None: #en este ejercicio asumo que solo se actualizará el teléfono
                        phone = input("Dime el teléfono del contacto: ")
                        phone = phone_checker(phone)
                    add_new_contact(agenda, Contact(name, phone))
                    break
                case "N":
                    break
                case _:
                    option = input(f"Tu opción no es válida. ¿Quieres añadir a {name} como nuevo contacto?(S/N): ")
    else:
        print("Datos actuales del contacto:")
        agenda.show_contact(index)
        if phone == None:
            phone = input(f"Dime el nuevo teléfono: ")
            phone = phone_checker(phone)
        print("Actualizando contacto...")
        sleep(2)
        agenda.update_contact(Contact(name, phone))
        print("¡Contacto actualizado!\n")

def delete_contact(agenda: Agenda, name: str):
    try:
        find_contact(agenda, name)
    except:
        print("El contacto no ha sido encontrado")
    else:
        option = input("¿Seguro que quieres borrar este contacto?(S/N): ").upper()
        while option != "N":
            match option:
                case "S":
                    agenda.delete_contact(name)
                    print("Contacto borrado\n")
                    break
                case "N":
                    break
                case _:
                    option = input(f"Tu opción no es válida. ¿Quieres borrar el contacto de {name}?(S/N): ")

print("##################################################")
print("Te doy la bienvenida al sistema de Agenda de avcenal.dev")
my_agenda = Agenda()
option = ""

while option != "S":
    print("Opciones:\n\n- Mostrar Agenda Completa (M)\n- Nuevo contacto (N)\n- Buscar contacto (F)\n- Actualizar contacto (U)\n- Borrar contacto (E)\n- Salir (S)\n\n")
    option = input("¿Que quieres hacer? Introduce tu opción: ").upper()
    print("\n")
    match option:
        case "M":
            show_full_agenda(my_agenda)
        case "N":
            name = input("Perfecto, dime el nombre del contacto que quieres añadir: ").title()
            phone = input("Y ahora el teléfono de este nuevo contacto: ")
            phone = phone_checker(phone)
            add_new_contact(my_agenda, Contact(name, phone))
        case "F":
            name = input ("Ok, dime el nombre que quieres buscar en la agenda: ").title()
            find_contact(my_agenda, name)
        case "U":
            name = input ("Entendido, dime el nombre del contacto que quieres actualizar: ").title()
            update_contact(my_agenda, name)
        case "E":
            name = input ("Adelante, dime el nombre del contacto que quieres borrar: ").title()
            delete_contact(my_agenda, name)
        case "S":
            break
        case _:
            print("Tu opción no es válida, probemos de nuevo...\n")

print("Gracias por utilizar este sistema de agenda. ¡Hasta pronto!\n")