import pandas as pd
import numpy as np
# info={
#     "Name":["Nick","John","David"],
#     "Marks":[78,52,65],
#     "Grade":['A','B','C']
# }
# df=pd.DataFrame(info)
# print(df)
# print(type(df))
# print(df.index)
# print(df.columns)


# From List of List
# df=pd.DataFrame([["Nick",23],["John",25]],columns=["Name","Age"])
# print(df)

# From Numpy Array
# np.arr=np.array([[1,2,3],[4,5,6]])
# df=pd.DataFrame(np.arr,columns=["A","B","C"])
# print(df)


# working Data Files

# Its used to import data from CSV File
# df_csv=pd.read_csv("movie.csv")  
# print(df_csv)    

# Importing data from json file
# df_json= pd.read_json("data.json")
# print(df_json)

# for exporting data to csv file
# df.to_csv("movie.csv")
# Exporting data from json file
# df.to_csv("movie.json")


# dataframe methods

# data={
#     'name':['Nick','John','David',"lili","ana","mariam"],
#     "age": [45,25,22,25,24,65],
#     "city":["Mohali","Delhi","Ludhiana","bangalore","chandigarh","hathoa"]
# }
# df=pd.DataFrame(data)
# print(df.head(2))    
# Basically , its used too show first n rows. By default it show 5 rows 

# print(df.tail(1))
# print()
#  Basically , its used too show last  n rows.

# print(df.sample())
# print()
#  Shows random n rows(by default=1)

# print(df.info())
# display column,numes,datatypes,memory uasge

# print(df.describe())
# shows descriptive statistics for numeric column like mean

# print(df.unique())
# shows count of distinct values exist in each column


# slicing Columns

# df["name"]  
# returns the series

# df[["city","age"]]
# returns the dataframe

# Practice Excercise

# Question no-1(basics)
# data={
#     'name':['Nick','John','David',"lili","ana","mariam"],
#     "age": [45,25,22,25,24,65],
#     "city":["Mohali","Delhi","Ludhiana","bangalore","chandigarh","hathoa"]
# }
# df=pd.DataFrame(data)
# print(df)
# print()
# print("Name",df["name"])
# print()
# print("First two rows: ")
# print(df.head(2))
# print()
# print("Last row: ")
# print(df.tail(1))
# print()
# print("Number of row and columns: ")
# print(df.shape)
# print()
# print("Column names: ")
# print(df.columns)
# print()
# print("Data types of Columns: ")
# print(df.dtypes)
# print()
# print("Summary Information:")
# print(df.info())

# question-2(selection)

# data={
#     'name':['Nick','John','David',"lili","ana","mariam"],
#     "age": [45,20,22,25,24,65],
#     "city":["Mohali","Delhi","delhi","bangalore","chandigarh","hathoa"]
# }
# df=pd.DataFrame(data)
# print("display only the name nadd city column")
# print(df[["name","city"]])
# print()
# print("Details of student in row index 1")
# print(df.loc[0])
# print()
# print("Display student age greater than 20: ")
# print(df [df["age"]>20])
# print()
# print("Students Whose City is Delhi:")
# print(df [df["city"]=="delhi"])
# print()
# print("Maximum Age: ")
# print(df["age"].max())
# print()
# print("Minimum age:")
# print(df["age"].min())


# question-3(adding and updating)

# data={
#     'name':['Nick','John','David',"lili","ana","mariam"],
#     "age": [45,20,22,25,24,65],
#     "city":["Mohali","Delhi","delhi","bangalore","chandigarh","hathoa"]
# }
# df=pd.DataFrame(data)
# df["Marks"]=[85,25,98,74,54,25]
# print("Adding New Column")
# print(df)
# print()
# print("Adding new student :")
# new_stu={
#     "name":"laila",
#     "age":45,
#     "city":"Londan",
#     "Marks":88
# }
# df.loc[len(df)]=new_stu
# print(df)
# print()
# print("Update age of Nick")
# df.loc[df["name"]=="Nick","age"]=20
# print(df)
# print()
# print("Change City of John: ")
# df.loc[df["name"]=="John","city"]="mumbai"
# print(df.loc[1])
# print()
# print("Increase Student marks by 10:")
# df["Marks"]=df["Marks"]+10
# print(df)
# print()
# print("Deleting the column")
# df=df.drop("city",axis=1)
# print (df)
# print()
# print("deleting the row")
# df=df.drop(2)
# print(df)
# print()
# print("Delete Student Whose age is less than 20")
# df=df[df["age"]>20]
# print(df)

#  question-4(function)
#data={
#     'name':['Nick','John','David',"lili","ana","mariam"],
#     "age": [45,20,22,25,24,65],
#     "city":["Mohali","Delhi","delhi","bangalore","chandigarh","hathoa"],
#     "marks":[55,66,25,74,85,94]
# }
# df=pd.DataFrame(data)
# print("average age: ")
# Average_marks=df["age"].mean()
# print(Average_marks)
# print()
# print("Total marks")
# Total_marks=df["marks"].sum()
# print(Total_marks)
# print()
# print("Sort Data Frame by Marks:")
# sort=df.sort_values(by="marks")
# print(sort) 

import csv
data={
    'name':['Nick','John','David',"lili","ana","mariam"],
    "age": [45,20,22,25,24,65],
    "city":["Mohali","Delhi","delhi","bangalore","chandigarh","hathoa"],
    "marks":[55,66,25,74,85,94]
}
df=pd.DataFrame(data)
df. to_csv("students.csv",index=False)
df=df_csv=pd.read_csv("students.csv")
print(df)
print()
print("Display Only first 5 Rows:")
df=(df.head())
print(df)
print()
print("Display last three rows")
df=(df.tail(3))
print(df)
print()
print(df.isnull())