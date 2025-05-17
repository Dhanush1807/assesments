class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee Name {self.name}\nEmployee ID - {self.emp_id}\n Annual Salary = {self.salary}"
    
    def __len__(self):
        print(len(self.name))

    def __add__(self,incentives = 1000):
        return self.salary + incentives



e1 = Employee(123,"John Doe",50000)
e2 = Employee(124,"Robert",70000)

print(e1)
print(e2)
print(e1 + 1000)