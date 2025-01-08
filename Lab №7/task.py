class Employee:
    def __init__(self, pname, id):
        self.pname = pname
        self.id = id
    def get_info(self):
        return [self.pname, self.id]

class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} is managing a project in the {self.department} department."

class Technician(Employee):
    def __init__(self, specialization):
        self.specialization = specialization
    def perform_maintenance(self):
        print('Производит техническое обслуживание...')

class TechManager(Manager,Technician):
    pass

Programmer = Employee("Andrew", "0451")
print(Programmer.get_info())
Boss = Manager('huy',2,'ifnewi')
print(Boss.get_info)
#Boss = Manager("Marketing")
#Tech = Technician("Software Engineer")
#BigBoss = TechManager('IT')
#
#print(Programmer.get_info())
#Boss.manage_project()
#Tech.perform_maintenance()
#BigBoss.add_employee('Dude')
#BigBoss.manage_project()


