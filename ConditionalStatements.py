#Conditional Statement- are used to make decision based on whether the condition is True or false
#if statement-It's used to execute the block of the code only if the condition is true
age=20
if age>=20:
    print("person is eligible for vote")


#if-else statement-In this if one condition is true then if block will execute otherwise else will execute
age1=18
if age1>=20:
    print("eligible for vote")
else:
    print("not eligible for vote")


#if-elif-else -This statement is used when you want to check multiple condition
marks =78
if marks>95:
    print("Grade A")
elif marks>85:
    print("Grade B")
elif marks>75:
    print("Grade c") 
elif marks>50:
    print("Grade D")
else:
    print("fail")


#Nested if -it's placed inside the another if satement
age=int(input("Enter age of the person: "))
citizen=input("Are you Indian (yes/no): ")
if age>=18:
    if citizen.lower()=="yes":
        print("Eligible for vote: ")
    else:
        print("Not Eligible")
else:
    print("Under age")


#logical Operator OR
day= input("Enter day: ")
if day.lower()=="saturday" or day.lower()=="sunday":
    print("Weekend")
else:
    print("Weekday")


#Logical Operator- And
username= input("Enter username: ")
password=input("enter password: ")
if username=="abc" and password=="123":
    print("login succesfully")
else:
    print("Invalid")
    

#Logical Operator- Not
is_logged_in= False
if not is_logged_in:
    print("please login")
else:
    print("Welcome")
    









