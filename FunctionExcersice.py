# Exercise 1:
# Write a function named welcome() that displays the message:
# "Welcome to Python Programming!"
# Call the function three times.

# def welcome():
#     print("WELCOME TO PYTHON PROGRAMMING!")
# welcome()
# welcome()
# welcome()


# Exercise 2:
# Write a function greet(name) that accepts a person's name as a parameter and displays a personalized greeting message.

# def greet(name):
#     print("Thank you\nPlease visit again!\n",name)
# greet("Lifestyle Garments")


# Exercise 3:
# Write a function add(a, b) that accepts two numbers and returns their sum. Display the returned value in the main program.
# def add(a,b):
#     print("Sum is:",a+b)
# add(10,20)


# Exercise 4:
# Write a function that accepts three numbers as parameters and returns the largest number.
# def largest(a,b,c):
#     if a>b and a>c:
#         print("value of a is greater")
#     elif b>a and b>c:
#         print("value of b is greater")
#     else:
#         print("value of c is greater")
# largest(85,9,54)


# Exercise 5:
# Write a function calculate_interest(principal, time, rate=5) to calculate Simple Interest.
# Call the function once using the default rate.
# Call the function again using keyword arguments with a custom rate.

# def calculate_interest(principal,time,rate=5):
#     print("interst is = ",(principal*rate*time)/100)
# calculate_interest(10000,1)
# calculate_interest(10000,1,4)


# Exercise 6:
# Write a function using *args that accepts any number of integers and displays:
# The total number of values entered.
# The sum of all the values.

# def total(*numbers):
#     print(sum(numbers))
#     print("Total number of value entered: ",len(numbers))
# total(10,50,60)


# Exercise 7:
# Write a function using **kwargs to accept and display employee details such as:
# Name
# Department
# Salary

# def employee_details(**info):
#     print(info)
# employee_details(name="nick",department="Finance",salary=10000)

# Exercise 8:
# Write a program that demonstrates the difference between a local variable and a global variable by printing their values inside and outside a function.
# num1=100
# def sum():
#     num2=20
#     print("Global Variable  is =",num1)
#     print("Local Variable is = ",num2)
#     print("addition is = ",num1+num2)
# sum()
# print("Global Variable  is =",num1)


# Exercise 9:
# Create a global variable named counter. Write a function that increments the value of counter each time it is called using the global keyword. Call the function five times and display the updated value

counter=0
def increment():
    global counter
    counter+=1
increment()
increment()
increment()
increment()
increment()
increment()
print(counter)


# Exercise 10:
# Write lambda functions to perform the following operations:
# Find the square of a number.
# Find the larger of two numbers

# square=lambda a:a*a
# print(square(3))
# larger_number=lambda a,b: a if a>b else b
# print(larger_number(10,20))