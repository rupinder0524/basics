# #Excercise- 01
# #Temperature checker
# temp=int(input("Enter Temprature in celcius: "))
# if temp>35:
#     print("Hot Weather")
# elif temp>=20 and temp<=35:
#     print("Pleasant weather")
# else:
#     print("Cold Weather")
    

# #Excecise- 02
# #Movie Ticket Eligibility
# age=int(input("Enter the age of the person: "))
# if age<5:
#     print("Free Ticket")
# elif age>=5 and age<=17:
#     print("Child Ticket")
# elif age>=18 and age<=59:
#     print("Adult Citizen")
# else:
#     print("Senior citizen")


# #Excercise no-03
# #Laptop Price Discount
# price=int(input("Enter the price of the laptop: "))
# if price>=80000:
#     discount1=20
#     discount1_amount=price*discount1/100
#     final_price=price-discount1_amount
#     print("Discount Percentage: ")
#     print("Original amount: ",price)
#     print(" Final price : ",final_price )
# elif price>=50000 and price<=79999:
#     discount2=10
#     discount2_amount=price*discount2/100
#     final_price2=price-discount2_amount
#     print("Discount percentage: ",discount2)
#     print("Original amount: ",price)
#     print("Amount after applying discount: ",final_price2)
# else:
#     print("Original amount (NO discount applied ): ",price)


# #Excercise no-04
# #Cricket Team Selection
# age=int(input("Enter age of the person: "))
# fitness_status=input("Tell your fitness status(yes/No): ")
# if age>18 and age<35 and fitness_status.lower()== "yes":
#     print("selected")
# else:
#     print("Not Selected")


# #Excercise no-05
# #Mobile number Validation
# mob_num=input("Enter mobile number: ")
# if len(mob_num)==10:
#     print("valid Mobile number")
# else:
#     print("inavlid")


# #Excercise no-06
# #Favourite Programming Language
# languages=["python","Java","c++","javascript","go"]
# FavLanguage=input("Enter Your Favourite Programming Language: ")
# if FavLanguage in languages:
#     print("Available")
# else:
#     print("Not Available")



# #Excercise no-7
# #Product Information
# product={
#     "name":"Laptop",
#     "price": 55000,
#     "brand":"Dell"
# }
# print("Name of product: ",product["name"])
# print("Name of Brand: ",product["brand"])
# print("Price of the product: ",product["price"])
# product1={"price":60000}
# product.update(product1)
# print("After updation: ",product1["price"])



# #Excercise no-08
# #Remove Duplicate Numbers
# numbers=[10,20,30,20,10,40,50]
# num1=set(numbers)
# print(num1)


#Excercise no-09
#Student Course Check
courses=("python","AI","Data Science","Machine Learning")
CourseName=input("Enter the Name of your Course: ")
if CourseName in courses:
    print("Course Available")
else:
    print("Course not Available")



# #Excecise no-10
# #Electricity Bill Category
# billamount=int(input("Enter the amount of the bill: "))
# if billamount >= 0 and billamount <=99:
#     print("Low Bill")
# elif billamount >=1000 and billamount <= 2999:
#     print("Medium Bill")
# else:
#     print("High Bill")
