# # Excersice-1
# def Company_Details(**kwargs):
#     for key,value in kwargs.items():
#         print(key,":",value)
# Company_Details(CompanyName="Net Square Softwares",Location="Mohali",Employees="John ,Nick,Ella",CEO="Inderpal Taur",FounderYear=2025)

# Excercise-2
# class Animal:
#     def eat(self):
#         print("Animal is Eating")
# class dog(Animal):
#     def bark(self):
#         print("Dog is barking")
# class cat(Animal):
#     def meow(self):
#         print("Cat is Meowing ")
# class elephant(Animal):
#     def Trumphet(self):
#         print("Elephant is trupting")
# Dog = dog()
# Cat=cat()
# Elephant=elephant()

# Dog.eat()
# Dog.bark()

# Cat.eat()
# Cat.meow()

# Elephant.eat()
# Elephant.Trumphet()


# Excersice-3

# class CreditCard():
#     def pay(self):
#         print("paid using Credit Card")
# class UPI():
#     def pay(self):
#         print("Paid using UPI")
# class Cash():
#     def pay(self):
#         print("Paid using Cash")
# creditCard=CreditCard()
# upi=UPI()
# cash=Cash()

# creditCard.pay()
# upi.pay()
# cash.pay()

# Excersice-4
# student=["nick","john","Rabia","Maria","David"]
# with open("Student.txt","w")as file:
#   for name in student:
#     file.write(name+"\n")
# with open("Student.txt","r")as file:
#         for line in file:
#             print(line)

# class SmartTV:
#     def __init__(self):
#         self.__volume=20
#     def increase_volume(self):
#         if self.__volume<100:
#             self.__volume+=1
#         else:
#             print("Volume is full")
#     def decrese_volume(self):
#         if self.__volume>0:
#             self.__volume-=1
#         else:
#             print("Volume is already zero")
#     def show_volume(self):
#         print("Show Volume",self.__volume)
# tv=SmartTV()
# tv.increase_volume()
# tv.show_volume()
# tv.decrese_volume()
# tv.show_volume()


# Excercise-6
# import csv
# with open("product.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(["ProductID","ProductName","Price","Quantity"])
#     writer.writerow([101,"Chair",1500,3])
#     writer.writerow([102, "Table", 3000, 2])
#     writer.writerow([103, "Sofa", 12000, 1])
# total_Stock_Value=0
# with open("product.csv","r")as file:
#     data=csv.reader(file)
#     for row in data:
#         if row[0] == "ProductID":
#             continue
#         Price=int(row[2])
#         Quantity=int(row[3])
#         total_Stock_Value+=Price*Quantity
# print("Total Stock Value: ",total_Stock_Value)


# Excercise-7
# import csv
# class patient:
#     def __init__(self,PatientID,Name,Disease,Age):
#         self.PatientID=PatientID
#         self.Name=Name
#         self.Disease=Disease
#         self.Age=Age
#     def display(self):
#         print("Patient ID:", self.PatientID)
#         print("Name:", self.Name)
#         print("Disease:", self.Disease)
#         print("Age:", self.Age)

# patient1=patient(101,"Nick","dengue",45)
# patient2=patient(102,"john","dengue",12)
# patient3=patient(103,"David","Dengue",22)
# patient4=patient(104,"Lilly","Dengue",25)
# patient5=patient(105,"Maria","Dengue",54)
# with open("patient.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow([patient1.PatientID,patient1.Name,patient1.Disease,patient1.Age])
#     writer.writerow([patient2.PatientID,patient2.Name,patient2.Disease,patient2.Age])
#     writer.writerow([patient3.PatientID,patient3.Name,patient3.Disease,patient3.Age])
#     writer.writerow([patient4.PatientID,patient4.Name,patient4.Disease,patient4.Age])
#     writer.writerow([patient5.PatientID,patient5.Name,patient5.Disease,patient5.Age])
# with open("patient.csv","r")as file:
#     reader = csv.reader(file)
#     next(reader)
#     for rows in reader:
#         p=patient(int (rows[0]),(rows[1]),(rows[2]),int(rows[3]))
#         p.display()


# Excercise-8
import csv
class movie:
    def __init__(self,MovieId,MovieName,Rating,Language):
        self.MovieId=MovieId
        self.MovieName=MovieName
        self.Rating=Rating
        self.Language=Language
    def display(self):
        print("Movie ID: ",self.MovieId)
        print("Movie Name:",self.MovieName)
        print("Rating:",self.Rating)
        print("Labguage: ",self.Language)

    def is_hit(self):
        if self.Rating >=8:
            print("hit movie")
        else:
            print("Average Movie")
    
movie1=movie(101,"abc",4,"rch")
movie2=movie(102,"ndh",5,"asj")
movie3=movie(103,"sgd",4,"gdh")
movie4=movie(104,"ghd",8,"gdd")
movie5=movie(105,"dhc",2,"dhj")

with open("movie.csv","w",newline="") as file:
   writer=csv.writer(file)
   writer.writerow([movie1.MovieId,movie1.MovieName,movie1.Rating,movie1.Language])
   writer.writerow([movie2.MovieId,movie2.MovieName,movie2.Rating,movie2.Language])
   writer.writerow([movie3.MovieId,movie3.MovieName,movie3.Rating,movie3.Language])
   writer.writerow([movie4.MovieId,movie4.MovieName,movie4.Rating,movie4.Language])
   writer.writerow([movie5.MovieId,movie5.MovieName,movie5.Rating,movie5.Language])

with open("movie.csv","r")as file:
    reader = csv.reader(file)
    next(reader)
    for rows in reader:
        m=movie(int (rows[0]),(rows[1]),int(rows[2]),rows[3])
        m.display()
        m.is_hit()