class Employee:
    def __init__(self, name: str, age: int, salary: float):
        "Initialize Employee with name, age, and salary"
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        "Return a string representation of the Employee instance"
        return f"Employee(name='{self.name}', age={self.age}, salary={self.salary})"

class HRSystem:
    def __init__(self):
        "Initialize HRSystem with an empty dictionary to store employees"
        self.employees: Dict[int, Employee] = {}

    def add_employee(self, emp_id: int, name: str, age: int, salary: float) -> None:
        """Add a new employee to the system."""
        self.employees[emp_id] = Employee(name, age, salary)

    def remove_employee(self, emp_id: int) -> None:
        """Remove an employee from the system by their ID."""
        if emp_id in self.employees:
            del self.employees[emp_id]

    def get_employee_info(self, emp_id: int) -> Any:
        """Retrieve information about an employee by their ID."""
        return self.employees.get(emp_id)
