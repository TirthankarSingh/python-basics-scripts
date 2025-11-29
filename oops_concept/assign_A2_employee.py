class Employee:
    def __init__(self,name,base_salary):
        self.name = name
        try:
            self.base_salary = float(base_salary)
        except (ValueError, TypeError):
            raise ValueError("Base salary should be a number")
        if self.base_salary <= 0:
            raise ValueError("base salary cannot be zero or negative number")

    def __str__(self):
        return f"Name: {self.name}, Base Salary: {self.base_salary}"

    def bonus(self):
        return 0.0


class Manager(Employee):
    def __init__(self,name,base_salary, team= None):
        super().__init__(name, base_salary)
        self.team = [] if team is None else team

    def add_member(self, name):
        self.team.append(name)

    def remove_member(self, name):
        if name in self.team:
            self.team.remove(name)
        else:
            raise ValueError("no such team member identified")

    def bonus(self):
        team_size = len(self.team)
        return 0.05 * self.base_salary + 100 * team_size

    def __str__(self):
        return f"Name: {self.name}; Base Salary: {self.base_salary}; Team size: {len(self.team)}"

class Intern(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def __str__(self):
        return f"intern(Name={self.name}, Stipend={self.base_salary})"

    def bonus(self):
        return 0.0

if __name__ == "__main__":
    alice = Employee("Alice", 50000)
    bob = Employee("Bob", 60000)
    i1 = Intern("Charlie", 1500)
    print(alice)
    print(bob)
    print(i1)

    mgr = Manager("Tirth", 250000,['Sonam'])
    mgr.add_member("Myra")
    mgr.remove_member("Hello")

