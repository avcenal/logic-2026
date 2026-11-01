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
* Dependiendo de su labor, / tienen propiedades y funciones exclusivas de su
* actividad, y almacenan los empleados a su cargo."""
from time import sleep

class Empleado():
    def __init__(self,name: str, id:int):
        self.name = name
        self.id = id

    def show_info(self):
        pass

    def clock_in(self, hour:str):
        print(f"{self.name} ficha entrada a las {hour}")

    def clock_out(self, hour:str):
        print(f"{self.name} ficha salida a las {hour}")

    def _check_existing_exmployee(self,id_new_employee:int, team: list):
        for employee in team:
            if employee.id == id_new_employee:
                return True

        return False

class Programador(Empleado):
    def __init__(self, name:str, id: int,languages:list):
        super().__init__(name, id)
        self.project = None
        self.languages = languages

    def develop_feature(self):
        print("Desarrollando feature")

    def solve_bug(self):
        print("Resolviendo bug")

    def testing(self):
        print("Haciendo tests")

class Gerente(Empleado):
    def __init__(self, name: str, id:int, department: str, team: list = None):
        super().__init__(name, id)
        self.department = department
        if team is None:
            self.team =  []
        else:
            self.team = team

    def show_info(self):
        if len(self.team) != 0:
            print(f"- Nombre: {self.name}\n- Id: {self.id}\n- Departamento: {self.department}\n- Equipo:\n")
            for index,employee in enumerate(self.team):
                print(f"{index}. {employee.name} - {employee.__class__.__name__}\n")
        else: 
            print(f"No hay empleados en el equipo de {self.name}")
    
    def have_meeting(self):
        print(f"{self.name} empieza la reunión")
        sleep(2)
        print(f"{self.name} termina la reunión")

    def hire_employee(self, employee:Empleado):
        if not self._check_existing_exmployee(employee.id,self.team):
            self.team.append(employee)
            print(f"{employee.name} contratado")
        else:
            print(f"{employee.name} ya está contratado")

    def fire_employee(self, employee:Empleado):
            self.team.remove(employee)

    def clock_in(self, hour):
        print(f"Siendo gerente no tienes que fichar la entrada a las {hour}")

    def clock_out(self, hour):
        print(f"Siendo gerente no tienes que fichar la salida a las {hour}")

class GerenteDeProyectos(Empleado):
    def __init__(self, name: str, id:int, team:list = None, projects: list = None):
        super().__init__(name, id)
        if team is None:
            self.team = []
        else:
            self.team = team
        
        if projects is None:
            self.projects = []
        else:
            self.projects = projects

    def assign_project(self,developer: Programador, project: str):
        developer.project = project
        if not self._check_existing_exmployee(developer.id, self.team):
            self.team.append(developer)

    def unassign_project(self,developer: Programador):
        if self._check_existing_exmployee(developer.id, self.team):
            developer.project = None
            self.team.remove(developer)
        else:
            print("El desarrollador no está en el equipo")

    def list_projects(self):
        print(self.projects)

manager = Gerente("Alex",123,"Growth")
manager2 = Gerente("Test", 987,"Tech")
manager.show_info()
manager.hire_employee(GerenteDeProyectos("Sole",456))
manager.hire_employee(Programador("Martin",789,["Python","Javascript"]))
manager.show_info()
manager.hire_employee(GerenteDeProyectos("Sole",456))
manager.show_info()
manager2.show_info()