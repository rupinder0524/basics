#what is python?
#python is a high level programming language.It's popular language which is easy to read and learn
#Variables 
# variables are like container which are used to store value 
num=5 
str1="hello world"
print("value of num is: ",num)
print("value of str is: ",str1)

name="Rupinder"
course="BCA"
collegeName="GNDEC"
print("my name is",name,"I am",course,"student in",collegeName )

#Basic Data Types
a=10   #int- use to store integer value
b="rupinder0524" #string-use to store the sequence of characters
c=52.5 #flaat-use to store Decimal number
d=False #boolean- it represent only two value true and false
e=None  #none-it represent absence of value or no value
 
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(d))

#List - it's ordered,mutable collection of the items .It can store different Data Types
color=["red","green","blue","white"]
print("color is: ",color)
print(color[1])
color[0]="pink"
print(color)

#tuples-It's ordered and immuteable collection of items
fruits=("mango","cherry","lemon","orange","kiwi")
print("Fruits: ",fruits)
print(fruits[3])


#sets-It's an unordered,mutable collection of unique items.
set1={1,"hello",2.54,"world"}
print(set1)
set1.add(2365)

#Dictionaries-It's key value pair 
student={"name": "Rupinder",
         "course" : "BCA",
         "college" :"GNDEC"}
print(student)
print(student.keys())
print(student.values())
print(student["name"])
print(student.items())

#Operators-Operators are used to perform operation on operands
#Arithemetic Operators- these are used to perform mathematical calculations on the operands
num1=20
num2=30
print("addition",num1+num2)
print("substraction: ",num1-num2)
print("Multiplication: ", num1*num2)
print("Divison: ",num1/num2)
print("modulas: ", num1%num2)
print("Exponent: ",num1**num2)

#Realational Operators- These are used to compare two or more values.It's also called Comaparison operator
num3=50
num4=70
print("Greater than operator: ",num3>num4)
print("Greater than equal to operator: ",num3>=num4)
print("less than operator: ",num3<num4)
print("less than equal to opeator: ",num3<=num4)
print("equal to equal to operator: ",num3==num4)

#Assignment Opeartor- It's is used assign values
num5=10
num5 +=5
print(num5)
num5 -=5
print(num5)
num5 *=5
print(num5)
num5 /=5
print(num5)
num5 %=5
print(num5)


#Logical operator- They are used to combine or compare two or more conditions and return a boolean avalue
num6=20
num7=80
print(num6>num7 and num6<num7)
print(num6>num7 or num6<num7)
print(not(num6>num7))


#Type Conversion- It's the process of converting a data type of value from one to another
#Implicit Conversion - It's automatically convert one data type to another
hindi=20
punjabi=30
english=50
Total=hindi+punjabi+english
print("total = ",Total)
average=Total/150
print("Average = ",average)
print(type(Total))
print(type(average))

#Explicit Conversion- In this user manually convert data type using built in function
num8=78
num9="20"
print(str(num8))
print(int(num9)+10)
print(float(num8))
