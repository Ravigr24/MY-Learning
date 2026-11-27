class employee():

    company_name = "XYZ"
    

    def __init__(self,emp_name,emp_dept):
        
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    # Alternative to class method
    def changes(self,new_company):
        employee.company_name = new_company

    @classmethod
    def changesInClass(cls,new_company):
        cls.company_name = new_company

    def info(self):
        print(f"Employee {self.emp_name} works for {self.emp_dept} department in {self.company_name}") # we use self for inner parameters

    @staticmethod
    def addition(x,y):
        print(x+y)



emp1 = employee("Ravikrian", "IT")
emp2 = employee("Kushi" , "IT")

emp1.addition(1,2)

emp1.changes("New company")
emp1.changesInClass("New_Company_2")
emp1.info()
emp2.info()

