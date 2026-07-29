#Exercise-2
#  Dataset Analysis
# Create a dataset containing

# Student Name
# Age
# Study Hours
# Attendance
# Final Marks
# City
# Answer:

# Dataset
# Observation
# Features
# Target
# Number of observations
# Number of features

# import pandas as pd
# data={
#     "Student Name":["Nick","John","Mariam","Raseed","Lilly"],
#     "Age":[20,30,21,22,24],
#     "Study Hours":[2,3,4,5,6],
#     "Attendance":["90%","70%","60%","75%","95%"],
#     "Final Marks":[50,60,70,80,90],
#     "City":["Mumbai","Gaziabad","Hyderabad","Mohali","Chandigarh"]
# }
# df=pd.DataFrame(data)
# print("DataSet:")
# print(df)
# print()
# print("Observations")
# observations = len(df)  
# print(observations)
# print()
# print("Features")
# features = ["Age", "Study Hours", "Attendance", "City"]
# print(features)
# print()
# print("Target")
# target = "Final Marks"
# print(target)
# print()
# print("Number of features")
# print(len(features))
# print()
# print("Number of Target")
# print(len(target))

# exercise-3

# Feature Selection Challenge
# For each problem identify X and y.
# Example:
# Predict House Price
# Columns

# Area
# Bedrooms
# Bathrooms
# City
# Price
# Questions
# What are the Features?
# What is the Target?

import pandas as pd
# df = pd.read_csv("House Price.csv")
# print(df)
# print()
# # Features-In Machine Learning (ML), features are simply the information (inputs) that you give to the computer so it can make a prediction.
# print("Features(X):")
# X=df[["Area","Bedrooms","Bathrooms","City"]]
# print(X)
# print()
# # Target= Target is the answer or result that a machine learning model tries to predict.
# print("Target(Y):")
# Y=df["Price"]
# print(Y)
# print()


# df2=pd.read_csv("car.csv")
# print(df2)
# print()
# print("Features(X):")
# X=df2[["Car_Model","Year","Mileage","Engine_CC","Fuel_Type","Brand"]]
# print(X)
# print()
# print("Target(Y):")
# Y=df2["Price"]
# print(Y)
# print()

# df3=pd.read_csv("Employee Salary.csv")
# print(df3)
# print()
# print("Features(X):")
# X=df3[["Employee_ID","Age","Experience_Years","Education","Department"]]
# print(X)
# print()
# print("Target(Y):")
# Y=df3["Salary"]
# print(Y)
# print()


# df1=pd.read_csv("Diabetes Prediction.csv")
# print(df1)
# print()
# print("Target(X):")
# X=df1[["Patient_ID","Age","Gender","BMI","Glucose_Level","Blood_Pressure","Insulin"]]
# print(X)
# print()
# print("Target(Y):")
# Y=df1["Diabetes"]
# print(Y)
# print()


# df4=pd.read_csv("loan.csv")
# print(df4)
# print()
# print("Features(X):")
# X=df4[["Applicant_ID","Age","Income","Credit_Score","Loan_Amount","Employment","Loan_Term"]]
# print(X)
# print()
# print("Target(Y):")
# Y=df4["Loan_Approval"]
# print(Y)
# print()


# df5=pd.read_csv("Movie Collection.csv")
# print(df5)
# print()
# print("Features(X):")
# X=df5[["Movie_ID","Genre","Budget_Million","Duration_Min","Rating","Release_Year"]]
# print(X)
# print()
# print("Target(Y):")
# Y=df5["Collection_Million"]
# print(Y)
# print()


# Exercise-4
# Regression or Classification?
# Decide whether each problem is
# Regression
# or
# Classification

# Predict Salary
# import pandas as pd
# df=pd.DataFrame("Employee Salary.csv")
# print(df)
# print()
# print("Target")
# target=df[["Employee_ID","Age","Experience_Years","Education","Department"]]
# print(target)
# print()
# print("Features")
# feature=df["Salary"]
# print()
# print("Problem Type")
# print("Regression")
#Salary is a numerical value, so the problem is Regression.


# Predict Blood Group
# import pandas as pd
# df=pd.read_csv("Blood_Group.csv")
# print(df)
# print()
# print("Features")
# feature=df[["Patient_ID","Age","Gebder","Weight_Kg","Height_cm","Blood_Pressure","Disease_Status"]]
# print(feature)
# print()
# print("Target")
# target=df["Blood_Group"]
# print(target)
# print()
# print("Problem Type")
# print("Classification")


# Predict Age

# import pandas as pd
# df=pd.read_csv("Blood_Group.csv")
# print(df)
# print()
# print("Features")
# feature=df[["Patient_ID","Age","Gebder","Weight_Kg","Height_cm","Blood_Pressure","Disease_Status"]]
# print(feature)
# print()
# print("Target")
# target=df["Blood_Group"]
# print(target)
# print()
# print("Problem Type")
# print("Classification")

# Predict Height

# import pandas as pd
# df=pd.read_csv("Blood_Group.csv")
# print(df)
# print()
# print("Features")
# feature=df[["Patient_ID","Age","Gender","Weight_kg","Height_cm","Blood_Pressure","Disease_Status"]]
# print(feature)
# print()
# print("Target")
# target=df["Height_cm"]
# print(target)
# print()
# print("Problem Type")
# print("regression")


# Predict Pass/Fail
# Predict House Price
# Predict Disease
# Predict Temperature
# Predict Spam Email


# Exercise 5

# Collect Cricket Data
#         |
# EDA (Exploratory Data Analysis)
#         │        
# Select Features (X)
#         │         
# Select Target (y)
#         │
# Train-Test Split
#         │
# Train Machine Learning Model
#         │        
# Make Predictions
#         │        
# Evaluate Model Performance


# 1.Collect Cricket Data-
# intially,I collect Cricket Related Data such as:
# Player Name, Age,Player runs, wickets, matches played, strike rate, average and past match performance.

# 2.EDA(Explotriary Data Analysis)
# In this second step, We Analyze Collected Data means
# check Missing value then Fill it
# find Useful Information Related to data using describe(),info() etc

#3. Select Features(X)
# In this 3rd Step i select Important Features that help to make a prediction
# Moreover,features are simply the information (inputs) that you give to the computer so it can make a prediction.
# Example-Past match Performance

# 4. Select Target(Y)
# In this Step, I will select the Output That I want to predict
# For Example- If I want To Predict Player's Run in Next Match I will choose it as target
# Moreover-Target is the answer or result that a machine learning model tries to predict.

# 5.Train-Test Split
# In this step,I will divide the data in to two Main parts
# I. Training Data-It help Model to learn Pattern from previous match data
# II.Testing Data - It is used to check whether the model is giving correct predictions or no

# 6.Train Machine Learning Model
# In this step, I train the machine learning model using the training data.
# The model studies old cricket match data and learns patterns from it.
# It understands how different factors like runs, average, strike rate, and player performance affect the result.
# Example:
# The model learns from a player's past matches and understands how many runs the player may score in the next match


# 7.Make Prediction
# After Traaining the Model, it will predict the Future match Score of a player

# 8.Evaluate Model Performance
# At last, i will check the predicted result with the actual result and improve the model if required.


# Exercise-6
# Manual Prediction
# Suppose a model learns
# Salary = 6000 × Experience + 25000Predict salary for

# 2 years
# 4 years
# 6 years
# 8 years
# 10 years
# Then explain
# What does
# 6000
# represent?
# What does
# 25000

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset from CSV file
data = pd.read_csv("employee_experience.csv")

# Display dataset
print(data)


# Features (Input)
X = data[["Experience "]]

# Target (Output)
Y = data["Salary "]


# Split dataset into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)


# Create Linear Regression model
model = LinearRegression()


# Train the model
model.fit(X_train, Y_train)


# Test the model
Y_pred = model.predict(X_test)


# Display actual and predicted salary
print("Actual Salary:")
print(Y_test)

print("\nPredicted Salary:")
print(Y_pred)


# Predict salary for new experience values
new_employee = pd.DataFrame({
    "Experience": [2, 4, 6, 8, 10]
})

prediction = model.predict(new_employee)


# Display predictions
for exp, salary in zip(new_employee["Experience"], prediction):
    print("Experience:", exp, "Years --> Predicted Salary: $", round(salary))