from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# Department functions

def list_departments():
    departments = Department.get_all()
    if departments:
        for department in departments:
            print(department)
    else:
        print("No departments found.")


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    if department:
        print(department)
    else:
        print(f'Department "{name}" not found')


def find_department_by_id():
    try:
        id_ = int(input("Enter the department's id: "))
        department = Department.find_by_id(id_)
        if department:
            print(department)
        else:
            print(f'Department with id {id_} not found')
    except ValueError:
        print("Invalid input. Please enter a valid integer id.")


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print(f"Error creating department: {exc}")


def update_department():
    try:
        id_ = int(input("Enter the department's id: "))
        department = Department.find_by_id(id_)
        if department:
            name = input("Enter the department's new name (press enter to keep current): ")
            location = input("Enter the department's new location (press enter to keep current): ")
            
            if name:
                department.name = name
            if location:
                department.location = location

            department.update()
            print(f'Success: {department}')
        else:
            print(f'Department with id {id_} not found')
    except ValueError:
        print("Invalid input. Please enter a valid integer id.")
    except Exception as exc:
        print(f"Error updating department: {exc}")


def delete_department():
    try:
        id_ = int(input("Enter the department's id: "))
        department = Department.find_by_id(id_)
        if department:
            department.delete()
            print(f'Department with id {id_} deleted')
        else:
            print(f'Department with id {id_} not found')
    except ValueError:
        print("Invalid input. Please enter a valid integer id.")
    except Exception as exc:
        print(f"Error deleting department: {exc}")


# Employee functions

def list_employees():
    employees = Employee.get_all()
    if employees:
        for employee in employees:
            print(employee)
    else:
        print("No employees found.")


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f'Employee "{name}" not found')


def find_employee_by_id():
    try:
        id_ = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(id_)
        if employee:
            print(employee)
        else:
            print(f'Employee with id {id_} not found')
    except ValueError:
        print("Invalid input. Please enter a valid integer id.")


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    try:
        department_id = int(input("Enter the employee's department id: "))
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')
    except ValueError:
        print("Invalid input. Please enter a valid integer for department id.")
    except Exception as exc:
        print(f"Error creating employee: {exc}")


def update_employee():
    try:
        id_ = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(id_)
        if employee:
            name = input("Enter the employee's new name (press enter to keep current): ")
            job_title = input("Enter the employee's new job title (press enter to keep current): ")
            department_id = input("Enter the employee's new department id (press enter to keep current): ")
            
            if name:
                employee.name = name
            if job_title:
                employee.job_title = job_title
            if department_id:
                employee.department_id = int(department_id)

            employee.update()
            print(f'Success: {employee}')
        else:
            print(f'Employee with id {id_} not found')
    except ValueError:
        print("Invalid input. Please enter valid integer values for id and department id.")
    except Exception as exc:
        print(f"Error updating employee: {exc}")


def delete_employee():
    try:
        id_ = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(id_)
        if employee:
            employee.delete()
            print(f'Employee with id {id_} deleted')
        else:
            print(f'Employee with id {id_} not found')
    except ValueError:
        print("Invalid input. Please enter a valid integer id.")
    except Exception as exc:
        print(f"Error deleting employee: {exc}")


def list_department_employees():
    try:
        dept_id = int(input("Enter the department's id: "))
        department = Department.find_by_id(dept_id)
        if department:
            print(f"Employees in {department.name}:")
            employees = department.employees
            if employees:
                for employee in employees:
                    print(f"- {employee}")
            else:
                print("No employees found in this department.")
        else:
            print(f'Department with id {dept_id} not found')
    except ValueError:
        print("Invalid input. Please enter a valid integer id.")
    except Exception as exc:
        print(f"Error listing department employees: {exc}")