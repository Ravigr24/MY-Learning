class employee():

    company_name = "XYZ"
    

    def __init__(self,emp_name,emp_dept):
        self.emp_name = emp_name
        self.emp_dept = emp_dept


    @property #Getter 
    def info(self):
        print(f"Employee {self.emp_name} works for {self.emp_dept} department in {self.company_name}") # we use self for inner parameters

    @info.setter #Setter
    def info(self,emp_details):
        new_empName, new_empDept = emp_details
        self.emp_name = new_empName
        self.emp_dept = new_empDept


    # def changeinfo(self,new_emp_name,new_emp_dept):
    #         self.emp_name = new_emp_name
    #         self.emp_dept = new_emp_dept

    @classmethod
    def changesInClass(cls,new_company):
        cls.company_name = new_company

    
    @staticmethod
    def addition(x,y):
        print(x+y)



emp1 = employee("Ravikrian", "IT")

emp1.info = ["Kushi", "IT"]
# print(emp1.info)
