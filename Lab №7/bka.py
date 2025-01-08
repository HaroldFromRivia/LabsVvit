class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Employee Name: {self.name}, ID: {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} is managing a project in the {self.department} department."

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} is performing maintenance in {self.specialization}."

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        # Employee.__init__(self, name, id)
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = [employee.get_info() for i in self.team]
        return team_info




employee = Employee("Alice", 1)
print(employee.get_info())


manager = Manager("Bob", 2, "IT")
print(manager.get_info())
print(manager.manage_project())


technician = Technician("Charlie", 3, "Networking")
print(technician.get_info())
print(technician.perform_maintenance())


tech_manager = TechManager("David", 4, "Engineering", "Software Development")
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())


tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)


print(tech_manager.get_team_info())