# # To store information of 1 student.


# # name = "Tanvir"
# # age = 20
# # course = "BCA"
# # marks = 85


# # Programming is not only about making code work!!!! 


# # Programming is about making code organised, reusable, readable and easy to maintain

# # OOP


# # OOP => Object Oriented Programming

# # OOP is a way of writing programs where every real-world thing becomes an object 



# # student
# # Car
# # Mobile
# # Bank Account


# # class = Data (Attributes) + Functions (Methods)


# # 4 Pillars of OOP

# # - Class ( A Blueprint for creating objects)

# class Student:
#     pass


# # Object ( A object is an instance of a class)

# student1 = Student()
# student2 = Student()

# # Attributes

# class Student:
#     pass

# student1 = Student()

# student1.name = "Tanvir"
# student1.age = 20

# print(student1.name)
# print(student1.age)


# # Constructor (init)

# # This is the most important part 


# # class Student:

# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age

# # student1 = Student("Rahul",21)
# # student2 = Student("Vaneet",20)


# # print(student1.name)
# # print(student2.name)


# # __init__ special method (Interview question)

# # Magic methods
# # Dunder methods


# # Extra 
# # __init__
# # __str__
# # __len__
# # __add__


# # Class => Object => Attributes => Constructor => Methods
# Excercise-1

# class student:
#     def __init__(self,name,age,course):

#         self.name=name
#         self.age=age
#         self.course=course
#     def display(self):
#         print("Name is: ",self.name)
#         print("age is: ",self.age)
#         print("Course: ",self.course)
# student1= student ("Nick",20,"BCA")
# student2=student("john",21,"BCA")
# student1.display()
# student2.display()


#  Excercise-2
# class car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def show_details(self):
#         print("Brand name is: ",self.brand)
#         print("model is: ",self.model)
#         print("Price is: ",self.price)
# car1= car("BMW","X1",4950000)
# car2=car("Audi","A4",4699000)
# car3=car("Mahindra","Scorpio N",1399000)
# car1.show_details()
# car2.show_details()
# car3.show_details()

#  Excercise-3

# class Mobile:
#     def __init__(self,brand,RAM,storage):
#         self.brand=brand
#         self.RAM=RAM
#         self.storage=storage
#     def call(self):
#         print(self.brand,"is calling")
#     def camera(self):
#         print(self.brand,"camera is opened")
# mobile1=Mobile("samsung",125,125)
# mobile1.call()
# mobile1.camera()

#Excercise-5
# class laptop:
#     def __init__(self,brand,processor,RAM,price):
#         self.brand=brand
#         self.processor=processor
#         self.RAM= RAM
#         self.price=price
#     def display(self):
#         print("Laptop Brand is : ",self.brand)
#         print("Laptop processor is: ",self.processor)
#         print("Latop RAM is: ",self.RAM)
#         print("Price of Laptop is: ",self.price)
# laptop1=laptop("Dell","Intel Core i5","8GB",59990)
# laptop1.display()

# Excercise-4
# class book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def display(self):
#         print("Title of the is: ", self.title)
#         print("author of the book is: ",self.author)
#         print("Price of the book is: ",self.price)
# book1=book("The Thousand splendied suns","Khalied Hossine",150)
# book1.display()


# Excercise=6
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("Name is",self.name)
#         print("marks is: ",self.marks)
    
#     def result(self):
#         if self.marks>=40:
#             print("Result is: pass")
#         else:
#             print("Result is:Fail")
# student1=student("Nick",49)
# student2=student("john",39)
# student1.display()
# student1.result()

# student2.display()
# student2.result()

# Excercise=7
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print("Name of Employee is: ",self.name)
#         print("Salary of Employee is: ",self.salary)
#     def bonus(self):
#         if self.salary>=50000:
#             print("After adding Bonus Salary is: ",(20*self.salary)/100 + self.salary)
#         else:
#             print("After adding Bonus Salary is: ",(20*self.salary)/100 + self.salary)
# emp1=employee("Nick",60000)
# emp2=employee("John",30000)
# emp1.display()
# emp1.bonus()
# emp2.display()
# emp2.bonus()

# Excercise=8
# class rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print("length of the rectangle is: ",self.length)
#         print("Width of rectnagle is : ",self.width)
#         area=self.width*self.length
#         print("Area of Rectangle is:",area)
#     def perimeter(self):
#         print("Perimeter of Rectangle is: ",2*(self.length+self.width))
# rect1=rectangle(20,20)
# rect1.area()
# rect1.perimeter()

# Excercise=9
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print("Radius of circle is: ",self.radius)
#         A=3.14*self.radius*self.radius
#         print("Area of circle is: ",A)
#     def circumference(self):
#         print("Circumference of circle is: ",2*3.14* self.radius)
# circle1=circle(20)
# circle1.area()
# circle1.circumference()


# Excercise-10

# class BankAccount:
#     def __init__(self,AccountHolder,Balance):
#         self.AccountHolder=AccountHolder
#         self.Balance=Balance
#     def deposit(self,amount):
#         print("Name of Account Holder is: ",self.AccountHolder)
#         self.Balance+=amount
#         print("Bank balance is:",self.Balance)
#     def withdraw(self,amount):
#         if amount>=self.Balance:
#             print("insufficent Balance")
#         else:
#             self.Balance-=amount
#             print("After Withdraw your Balance is :",self.Balance)
#     def show_Balance(self):
#         print("Bank Balace is: ",self.Balance)
# AccountHolder1=BankAccount("Nick",50000)
# AccountHolder1.deposit(10000)
# AccountHolder1.withdraw(20000)
# AccountHolder1.show_Balance()


# Excercise-11

# class student:
#     def __init__(self,name,RollNumber,Course,Marks):
#         self.name=name
#         self.RollNumber=RollNumber
#         self.Course=Course
#         self.Marks=Marks
#     def display(self):
#         print("Name is: ",self.name)
#         print("Roll Number: ",self.RollNumber)
#         print("Course: ",self.Course)
#         print("Marks: ",self.Marks)
# student1=student("Nick",21,"BCA",54)
# student2=student("John",22,"BCA",57)
# student3=student("Joy",23,"BCA",45)
# student4=student("Davidson",24,"BCA",97)
# student5=student("Lily",25,"BCA",65)

# students=[student1,student2,student3,student4,student5]
# for student in students:
#     student.display()


# class book:
#     def __init__(self,BookID,Title,Author,Price):
#         self.BookID=BookID
#         self.Title=Title
#         self.Author=Author
#         self.Price=Price
#     def display(self):
#         print("Book Id: ",self.BookID)
#         print("Title:",self.Title)
#         print("Author: ",self.Author)
#         print("Price:",self.Price)
# book1= book(101,"Ikigai","Hector Garcia",499)
# book2= book(102,"Atomic Habits","James Clear",699)
# book3= book(103,"Think like a Monk","jay shetty",566)
# book4= book(104,"The Alchemist","paulo Coelho",399)
# book5= book(105,"The Secret","Rhonda Byrne",450)

# books=[book1,book2,book3,book4,book5]
# for book in books:
#         book.display()

# Excercise-13
# class Employee:
#     def __init__(self, ID, Name, Department, Salary):
#         self.ID = ID
#         self.Name = Name
#         self.Department = Department
#         self.Salary = Salary
#     def display(self):
#         print("Employee Id:", self.ID)
#         print("Employee Name:", self.Name)
#         print("Employee Department:", self.Department)
#         print("Employee Salary:", self.Salary)
# emp1 = Employee(101, "John", "Finance", 20000)
# emp2 = Employee(102, "Nick", "Finance", 50000)
# emp3 = Employee(103, "Lily", "Finance", 60000)
# emp4 = Employee(104, "Davidson", "Finance", 70000)
# emp5 = Employee(105, "Ella", "Finance", 10000)
# employees = [emp1, emp2, emp3, emp4, emp5]
# for employee in employees:
#     if employee.Salary >= 50000:
#         employee.display()

# class product:
#     def __init__(self,ProductId,ProductName,Quantity,Price):
#         self.ProductId=ProductId
#         self.ProductName=ProductName
#         self.Quantity=Quantity
#         self.Price=Price
#     def display(self):
#         print("product id: ",self.ProductId)
#         print("Product Name", self.ProductName)
#         print("Quantity:",self.Quantity)
#         print("price: ",self.Price)
        
#     def stock_value(self):
#         value=self.Quantity*self.Price
#         print("stock value: ",value)
# product1=product(101,"Pen",5,10)
# product2=product(103,"pencil",7,10)

# products=[product1,product2]
# for product in products:
#     product.display()
#     product.stock_value()
    

# Excercise-15
class student:
    def __init__(self,RollNumber,Name,Course,Marks):
        self.RollNumber=RollNumber
        self.Name=Name
        self.Course=Course
        self.Marks=Marks
    def display(self):
        print("RollNumber:",self.RollNumber)
        print("Name:",self.Name)
        print("Course:",self.Course)
        print("Marks:",self.Marks)
    def grade(self):
        if self.Marks>=90:
            print("Grade A")
        elif self.Marks>75 and self.Marks<89:
            print("Grade B")
        elif self.Marks>54 and self.Marks<74:
            print("Grade C")
        else:
            print("fail")
student1=student(1,"Nick","BCA",57)
student2=student(2,"John","BCA",98)
student3=student(3,"David","BCA",65)
student4=student(4,"Lily","BCA",24)
student5=student(5,"Mariam","BCA",78)

students=[student1,student2,student3,student4,student5]
for student in students:
    student.display()
    student.grade()
highest_student = students[0]

for student in students:
    if student.Marks > highest_student.Marks:
        highest_student = student
print("\nHighest Marks Student")
highest_student.display()
print("Grade:", highest_student.grade())
total_marks = 0
for student in students:
    total_marks += student.Marks
average = total_marks / len(students)
print("\n Average Marks of All Students:", average)

        
