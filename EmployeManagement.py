class employee:
    def __init__(self,ID,Name,Departmrnt,Designation,Salary):
        self.ID=ID
        self.Name=Name
        self.Department=Departmrnt
        self.Designation=Designation
        self.Salary=Salary

# print("1.Add Employee")
# print("2.View Employee")
# print("3.Search Employee")
# print("4.Delete Employee")
# print("5.Delete Employee")
# print("6.Count Employee")
# print("7.Exit")

Employees=[]

def add_employee():
    ID=int(input("Enter ID of the employee: "))
    Name=input("Enter Name of the employee: ")
    Department=input("Enter Name of the department: ")
    Designation=input("Enter Employee Designation:")
    Salary=input(float("Enter Salary of the employee: "))
    emp=employee(ID,Name,Department,Designation,Salary)
    Employees.append (emp)

def View_Employee():
    if len(Employees)==0:
        print("No Employee Record")
    else:
        for emp in Employees:
            print("ID:",emp.ID)
            print("Name:",emp.Name)
            print("Department",emp.Department)
            print("Designation:",emp.Designation)
            print("Salry:",emp.Salary)
            

def Search_Employee():
    search_ID=int(input("Enter Employee ID to search: "))
    for emp in Employees:
        if search_ID==emp.ID:
            print("ID:",emp.ID)
            print("Name:",emp.Name)
            print("Department",emp.Department)
            print("Designation:",emp.Designation)
            print("Salry:",emp.Salary)
            return
        else:
            print("Employees Not Found")
            

def Update_Employee():
    Employe_Salary=int(input("Enter current Salary of the Employee: "))
    for emp in Employees:
        if Employe_Salary==emp.Salary:
           New_Slary=float(input("Enter New Salary: "))
           print("Update Salary is: ",New_Slary)
           print("Salary Updated Successfully!!")
        else:
            print("Employee Not Found")
            return

def Add_Bonus():
    employee_salary=float(input("Enter Salary of the employee: "))
    for emp in Employees:
        if employee>=50000:
             print("After adding Bonus Salary is: ",(20*employee_salary)/100 + employee_salary)
        else:
             print("After adding Bonus Salary is: ",(10*employee_salary)/100 +employee_salary)
             return

def delete_Employee():
    Employe_Id=int(input("Enter ID of the Employe: "))
    for emp in Employees:
        if emp.ID==Employe_Id:
            Employees.remove(emp)
            print("Employe Deleted Successfully!!")
        else:
            print("Employee Not Found")
            return
        
def Count_Employess():
    print("Total Employess are: ",len(Employees))

while True:
    print("1.Add Employee")
    print("2.View Employee")
    print("3.Search Employee")
    print("4.Update Salary")
    print("5. Add Bonus")
    print("6.Delete Employee")
    print("7.Count Employee")
    print("8.Exit")  

    choice=int(input("Enter Your Choice"))

    if choice==1:
        add_employee()
    
    elif choice==2:
        View_Employee()

    elif choice==3:
        Search_Employee()

    elif choice==4:
        Search_Employee()

    elif choice==4:
        Update_Employee()

    elif choice==5:
        Add_Bonus()

    elif choice==6:
        delete_Employee()

    elif choice==7:
        Count_Employess()

    elif choice==8:
        print("THANK YOU!")
        break

    else:
        print("Invalid Choice")

