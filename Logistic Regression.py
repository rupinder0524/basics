# problems = [
#     ["Disease", "No Disease"],
#     ["Cat", "Dog", "Horse"],
#     ["Pass", "Fail"],
#     ["Fraud", "Genuine"],
#     ["Red", "Blue", "Green"]
# ]

# for Problem in problems:
#     if len(Problem) == 2:
#         print("Binary Classification : ")
#         print(Problem)
#         print()
#     else:
#         print("Multiclass Classification :")
#         print(Problem)
#         print()

# exercise-2
# Threshold Prediction
# Using threshold = 0.5, predict the final class:
# Probability0.91,0.72,0.49,0.21,0.50
# Output:

# Predicted Class

# probabilities = [0.91, 0.72, 0.49, 0.21, 0.50]
# threshold = 0.5
# print("Probability\tPredicted Class")
# for p in probabilities:
#     if p >= threshold:
#         print(p, "\t\t", 1)
#     else:
#         print(p, "\t\t", 0)


# exercise-3
# Sigmoid Understanding
# Given:
# z-5-2025
# Write:

# Which values are likely Class 0?
# Which values are likely Class 1?
# Explain why
 
# import math
# z_values = [-5, -2, 0, 2, 5]
# for z in z_values:
#     probability = 1 / (1 + math.exp(-z))
#     if probability >= 0.5:
#         result = 1
#     else:
#         result = 0
#     print("z =", z)
#     print("Probability =",probability)
#     print("Predicted Class =", result)
#     print()



# Exercise 4: Feature & Target Selection
# Given a Heart Disease Dataset:
# AgeBPCholesterolHeart Disease
# Identify:

# Dataset
# Features (X)
# Target (y)
# Classification Type

# import pandas as pd
# import seaborn as sns
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, precision_score
# df = pd.read_csv("heart_disease.csv")
# print(df.columns)
# df.info()
# print(df.head(1))
# X = df[["Age", "BP", "Cholesterol"]]
# y = df["Heart Disease"]
# print("Number of classes:", y.nunique())
# print("\nTarget values:")
# print(y.head())
# # Split data
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )
# print("\nClass 1 values:")
# print(y_train[y_train == 1])
# print("\nClass 0 values:")
# print(y_train[y_train == 0])
# model = LogisticRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("\nAccuracy:", accuracy_score(y_test, y_pred) * 100, "%")
# print("Precision:", precision_score(y_test, y_pred) * 100, "%")


# Exercise 5: Train-Test Split Experiment
# Load the Heart Dataset.
# Create three different train-test splits:

# 80:20
# 70:30
# 60:40
# Train Logistic Regression on each.
# Compare:

# Accuracy
# Precision
# Which split performs best?


import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
df = pd.read_csv("heart_disease.csv")
print(df.head(1))
X = df[["Age", "BP", "Cholesterol"]]
y = df["Heart Disease"]
splits = [0.2, 0.3, 0.4]    
for test in splits:
        X_train, X_test, y_train, y_test = train_test_split(
        X, y,test_size=test,random_state=42
    )
        model = LogisticRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print("\nAccuracy:", accuracy_score(y_test, y_pred) * 100, "%")
        print("Precision:", precision_score(y_test, y_pred) * 100, "%")
     