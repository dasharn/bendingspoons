# Employee Management System

## Overview

This Python project implements a simple Employee Management System using object-oriented programming principles. It consists of two main classes: `Employee` and `HRSystem`, which together allow for the addition, removal, and retrieval of employee information.

## Classes

### Employee Class

The `Employee` class represents individual employees with attributes such as name, age, and salary. It provides a string representation of the employee object and encapsulates its data for robustness and maintainability.

#### Methods

- `__init__(self, name: str, age: int, salary: float)`: Initializes an employee with the given name, age, and salary.
- `__repr__(self) -> str`: Returns a string representation of the employee instance.

### HRSystem Class

The `HRSystem` class manages a collection of `Employee` objects using a dictionary. It provides functionality to add, remove, and retrieve employee information by employee ID.

#### Methods

- `__init__(self)`: Initializes an HRSystem instance with an empty dictionary to store employees.
- `add_employee(self, emp_id: int, name: str, age: int, salary: float) -> None`: Adds a new employee to the system.
- `remove_employee(self, emp_id: int) -> None`: Removes an employee from the system by their ID.
- `get_employee_info(self, emp_id: int) -> Any`: Retrieves information about an employee by their ID.

## Usage

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/employee-management.git
   cd employee-management
   ```

2. Ensure Python 3.x is installed. If not, download and install it from [python.org](https://www.python.org/downloads/).

3. No additional packages are required for this project.

### Example

```python
from employee_system import HRSystem

# Initialize HRSystem
hr_system = HRSystem()

# Adding employees
hr_system.add_employee(1, "Alice", 30, 50000.0)
hr_system.add_employee(2, "Bob", 25, 60000.0)
hr_system.add_employee(3, "Charlie", 35, 70000.0)

# Retrieving and printing employee information
emp_id = 2
employee_info = hr_system.get_employee_info(emp_id)
if employee_info:
    print(f"Employee {emp_id}: {employee_info}")
else:
    print(f"Employee with ID {emp_id} not found.")
```

