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
    def __init__(self, name:str, id: int,languages:list, project: str = None):
        super().__init__(name, id)
        """if projects is None:
            self.projects = []
        else:
            self.projects = projects"""
        self.project = project
        self.languages = languages

    def show_info(self):
        print("PROGRAMADOR")
        print(f"- Nombre: {self.name}\n- Id: {self.id}\nLenguajes:\n")
        for index,language in enumerate(self.languages):
            print(f"{index + 1}. {language}\n")
        print(f"Projecto: {self.project}\n")

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
            print("GERENTE")
            print(f"- Nombre: {self.name}\n- Id: {self.id}\n- Departamento: {self.department}\n- Equipo:\n")
            for index,employee in enumerate(self.team):
                print(f"{index + 1}. {employee.name} - {employee.__class__.__name__}\n")
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

    def show_info(self):
        print("GERENTE DE PROYECTOS")
        print(f"- Nombre: {self.name}\n- Id: {self.id}\n- Proyectos:\n")
        for index,project in enumerate(self.projects):
            print(f"{index + 1}. {project}\n")
        print("- Equipo:\n")
        for index, developer in enumerate(self.team):
            print(f"{index + 1}. {developer.name} - {developer.__class__.__name__}\n")

    def assign_project(self,developer: Programador, project: str):
        if developer.project is None:
            developer.project = project
        else:
            print(f"Este desarrollador ya tiene un proyecto asignado")
        if project not in self.projects:
            self.projects.append(project)
        else:
            print("El Project Manager ya está trabajando en este proyecto")
            
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
project_manager = GerenteDeProyectos("Sole",456)
developer = Programador("Martin",789,["Python","Javascript"])

#acciones de Gerente
manager.show_info()
manager.hire_employee(project_manager)
manager.hire_employee(developer)
manager.show_info()

#acciones de GerenteDeProyectos
project_manager.assign_project(developer, "WABA Flow feature")
project_manager.show_info()

#comprobación que el programador tiene asignado el proyecto que le ha asignado el Project Manager
developer.show_info()

#el project manager desasigna el proyecto del programador indicado
project_manager.unassign_project(developer)
project_manager.show_info()
developer.show_info()

#comprobación de que no se aceptan duplicados, en este caso en gerente
manager.hire_employee(project_manager)
manager.show_info()