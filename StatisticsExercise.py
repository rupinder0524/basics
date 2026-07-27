# import pandas as pd
# df=pd.read_csv("Real_Estate.csv")
# print(df)
# print()
# print(df.dtypes)
# print()
# print("Column Types:")
# types = {
#     "House_ID": "Nominal",
#     "City": "Nominal",
#     "Area (sq ft)": "Continuous",
#     "Bedrooms": "Discrete",
#     "Price": "Continuous",
#     "Age_of_House": "Continuous"
# }
# for column, dtype in types.items():
#     print(column, ":", dtype)
# print()
# print("Calculate Mean Price")
# print(df["Price"].mean())
# print()
# print(" Calculate Median Price")
# print(df["Price"].median())
# print()
# print("Calculate Mode of bed Rooms")
# print(df["Bedrooms"].mode())
# print()
# # Range
# # Variance
# # Standard Deviation of house prices.
# print("Calculate Range")
# print("Maximum Price",df["Price"].max())
# print("Minimum Price = ", df["Price"].min())
# print("Range =",df["Price"].max()-df["Price"].min())
# print()
# print("Calculate Variance")
# print(df["Price"].var())
# print()
# print("Calculate Standard Deviation of house Prices")
# print(df["Price"].std())
# print()
# print("Calculate Q1")
# Q1=df["Price"].quantile(0.25)
# print()
# print("Calculate Q2")
# Q2=df["Price"].quantile(0.50)
# print(Q2)
# print()
# print("Calculate Q3")
# Q3=df["Price"].quantile(0.75)
# print()
# print("Calculate IQR")
# IQR=Q3-Q1
# print(IQR)
# print()
# # Detect price outliers using the IQR method.
# # Explain whether the mean or median is a better measure of central tendency for house prices
# print("Detect price outliers using the IQR method.")
# lower_limit = Q1 - 1.5 * IQR
# upper_limit = Q3 + 1.5 * IQR
# outliers=df[(df["Price"]<lower_limit)|(df["Price"]>upper_limit)]
# print("Outlier Limits")
# print("Lower Limit:", lower_limit)
# print("Upper Limit:", upper_limit)
# print(outliers)
# print()
# print("Explain whether the mean or median is a better measure of central tendency for house prices")
# print()
# if len(outliers)>0:
#     print("Median is a better measure because house prices contain outliers.")
# else:
#     print("Mean is suitable because there are no major outliers.")

# Exercise-2

import pandas as pd
import numpy as np
df=pd.read_csv("mobile_company.csv")
print(df)
print()
print(df.dtypes)
print()
print("Column Types:")
types={
    "User_ID":"Nominal",
    "Daily_Screen_Time":"Numerical",
    "Number_Of_Apps": "Numerical",
    "Age":"Numerical",
    "Subscription_Type":"Categorical",
    "City":"Categorical"
}
for column, dtype in types.items():
    print(column, ":", dtype)
print()
print("Mean:")
print(df["Daily_Screen_Time "].mean())
print()
print("Median")
print(df["Daily_Screen_Time "].median())
print()
print("Mode")
print(df["Subscription_Type"].mode())
print()
print("Variance")
print(df["Daily_Screen_Time "].var())
print()
print("Standard Deviation")
print(df["Daily_Screen_Time "].std())
print()
print("10th percentile")
print(np.percentile ( df["Daily_Screen_Time "],10))
print()
print(" 25th percentile")
print(np.percentile( df["Daily_Screen_Time "],25))
print()
print(" 75th percentile")
print(np.percentile (df["Daily_Screen_Time "],75))
print()
print(" 95th percentile")
print(np.percentile(df["Daily_Screen_Time "],95))
print()
print("users with unusually high screen time.")
print("High Screen Time Users:")
Q1 = np.percentile(df["Daily_Screen_Time "], 25)
Q3 = np.percentile(df["Daily_Screen_Time "], 75)
IQR = Q3 - Q1
upper_limit = Q3 + (1.5 * IQR)
print("Upper Limit:", upper_limit)
high_users = df[df["Daily_Screen_Time "] > upper_limit]
print(high_users)