class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.deductions = 0
        self.tax_rate = 0.15  # Assuming a flat tax rate of 15%

    def calculate_net_salary(self):
        taxable_income = self.salary - self.deductions
        tax_amount = taxable_income * self.tax_rate
        net_salary = self.salary - tax_amount
        return net_salary

# Function to input employee data
def input_employee_data():
    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")
    salary = float(input("Enter employee salary: "))
    return name, employee_id, salary

# Function to manage deductions
def manage_deductions(employee):
    print(f"Current deductions for {employee.name}: ${employee.deductions}")
    new_deductions = float(input("Enter new deductions: "))
    employee.deductions = new_deductions

# Function to manage taxes
def manage_taxes(employee):
    new_tax_rate = float(input("Enter new tax rate (in decimal): "))
    employee.tax_rate = new_tax_rate

# Main program
employees = []

while True:
    print("\n1. Add Employee\n2. Manage Deductions\n3. Manage Taxes\n4. Calculate Net Salary\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name, employee_id, salary = input_employee_data()
        new_employee = Employee(name, employee_id, salary)
        employees.append(new_employee)
        print("Employee added successfully!")

    elif choice == 2:
        employee_id = input("Enter employee ID: ")
        found = False
        for employee in employees:
            if employee.employee_id == employee_id:
                manage_deductions(employee)
                found = True
                break
        if not found:
            print("Employee not found!")

    elif choice == 3:
        employee_id = input("Enter employee ID: ")
        found = False
        for employee in employees:
            if employee.employee_id == employee_id:
                manage_taxes(employee)
                found = True
                break
        if not found:
            print("Employee not found!")

    elif choice == 4:
        employee_id = input("Enter employee ID: ")
        found = False
        for employee in employees:
            if employee.employee_id == employee_id:
                net_salary = employee.calculate_net_salary()
                print(f"Net salary for {employee.name}: ${net_salary}")
                found = True
                break
        if not found:
            print("Employee not found!")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
