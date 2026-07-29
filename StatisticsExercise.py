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

# import pandas as pd
# import numpy as np
# df=pd.read_csv("mobile_company.csv")
# print(df)
# print()
# print(df.dtypes)
# print()
# print("Column Types:")
# types={
#     "User_ID":"Nominal",
#     "Daily_Screen_Time":"Numerical",
#     "Number_Of_Apps": "Numerical",
#     "Age":"Numerical",
#     "Subscription_Type":"Categorical",
#     "City":"Categorical"
# }
# for column, dtype in types.items():
#     print(column, ":", dtype)
# print()
# print("Mean:")
# print(df["Daily_Screen_Time "].mean())
# print()
# print("Median")
# print(df["Daily_Screen_Time "].median())
# print()
# print("Mode")
# print(df["Subscription_Type"].mode())
# print()
# print("Variance")
# print(df["Daily_Screen_Time "].var())
# print()
# print("Standard Deviation")
# print(df["Daily_Screen_Time "].std())
# print()
# print("10th percentile")
# print(np.percentile ( df["Daily_Screen_Time "],10))
# print()
# print(" 25th percentile")
# print(np.percentile( df["Daily_Screen_Time "],25))
# print()
# print(" 75th percentile")
# print(np.percentile (df["Daily_Screen_Time "],75))
# print()
# print(" 95th percentile")
# print(np.percentile(df["Daily_Screen_Time "],95))
# print()
# print("users with unusually high screen time.")
# print("High Screen Time Users:")
# Q1 = np.percentile(df["Daily_Screen_Time "], 25)
# Q3 = np.percentile(df["Daily_Screen_Time "], 75)
# IQR = Q3 - Q1
# upper_limit = Q3 + (1.5 * IQR)
# print("Upper Limit:", upper_limit)
# high_users = df[df["Daily_Screen_Time "] > upper_limit]
# print(high_users)

# exercise-3

# import pandas as pd
# import numpy as np
# df=pd.read_csv("athelets.csv")
# print(df)
# print()
# print(df.dtypes)
# print()
# print("Column Types:")
# types={
#     "Athelete":"Nominal",
#     "Country":"Categorical",
#     "Sport": "Categorical",
#     "Age":"Numerical",
#     "Height":"Numerical",
#     "Weight":"Numerical",
#      "Gold_Medals":"Numerical"
# }
# for column, dtype in types.items():
#     print(column, ":", dtype)
# print()
# print("Mean:")
# print(df["Age"].mean())
# print()
# print("Median")
# print(df["Height"].median())
# print()
# print("Mode")
# print(df["Sport"].mode())
# print()
# print("Range")
# print(df["Weight"].max()-df["Weight"].min())
# print()
# print("Variance")
# print(df["Height"].var())
# print()
# print("Standard Deviation")
# print(df["Age"].std())
# print()
# print("Calculate Q1")
# Q1=df["Gold_Medals"].quantile(0.25)
# print(Q1)
# print()
# print("Calculate Q2")
# Q2=df["Gold_Medals"].quantile(0.50)
# print(Q2)
# print()
# print("Calculate Q3")
# Q3=df["Gold_Medals"].quantile(0.75)
# print(Q3)
# print()
# print("IQR")
# IQR=Q3-Q1
# print(IQR)
# # Detect athletes with unusually high medal counts
# print("Detect athletes with unusually high medal counts")
# lower_limit = Q1 - 1.5 * IQR
# upper_limit = Q3 + 1.5 * IQR
# outliers=df[(df["Gold_Medals"]<lower_limit)|(df["Gold_Medals"]>upper_limit)]
# print("Outlier Limits")
# print("Lower Limit:", lower_limit)
# print("Upper Limit:", upper_limit)
# print()

# exercise-4
# import pandas as pd
# import numpy as np
# df=pd.read_csv("music.csv")
# print(df)
# print()
# print(df.dtypes)
# print()
# print("Column Types:")
# types={
#     "Song":"Nominal",
#     "Artist":"Nominal",
#     "Genre": "Categorical",
#     "Streams":"Categorical",
#     "Release_Year":"Categorical",
#      "Duration":"Numerical"
#   }
# for column in types.keys():
    # print(column, ":", types[column])
# print()
# print("Mean:")
# print(df["Streams"].mean())
# print()
# print("Median")
# # print(df["Duration "].median())
# # print()
# print("Mode")
# print(df["Genre"].mode())
# print()
# print("Range")
# print(df["Streams"].max()-df["Streams"].min())
# print()
# print("Variance")
# print(df["Streams"].var())
# print()
# print("Standard deviation")
# print(df["Streams"].std())
# print()
# print("5th percentile")
# print(np.percentile ( df["Streams"],5))
# print()
# print(" 25th percentile")
# print(np.percentile( df["Streams"],25))
# print()
# print(" 50th percentile")
# print(np.percentile (df["Streams"],50))
# print()
# print(" 90th percentile")
# print(np.percentile(df["Streams"],90))
# Q1 = df["Streams"].quantile(0.25)
# Q3 = df["Streams"].quantile(0.75)
# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
# outliers = df[(df["Streams"] < lower) | (df["Streams"] > upper)]
# print("Outlier Songs:")
# print(outliers[["Song", "Artist", "Streams"]])


# Exercise-5


# import pandas as pd
# import numpy as np
# df=pd.read_csv("Water Consumption.csv")
# print(df)
# print(df.dtypes)
# types={
#     "House_ID":"Nominal",
#     "Family_Size":"Numerical",
#     "Daily_Water_Usage":"Numerical",
#     "Area":"Categorical",
#     "Income_Group":"Categorical"

# }
# for column in types.keys():
#     print(column, ":", types[column])
# print()
# print("Mean:")
# print(df["Daily_Water_Usage"].mean())
# print()
# print("Median")
# print(df["Daily_Water_Usage"].median())
# print()
# print("Mode")
# print(df["Daily_Water_Usage"].mode())
# print()
# print("Range")
# print(df["Daily_Water_Usage"].max()-df["Daily_Water_Usage"].min())
# print()
# print("Variance")
# print(df["Daily_Water_Usage"].var())
# print()
# print("Standard deviation")
# print(df["Daily_Water_Usage"].std())
# print()


# Exercise-6

# import pandas as pd
# import numpy as np

# # Load dataset
# df = pd.read_csv("placement.csv")
# print(df)
# print("\nData Types:")
# print(df.dtypes)
# types = {
#     "Student": "Nominal",
#     "Branch": "Categorical",
#     "CGPA": "Continuous",
#     "Interview_Score": "Discrete",
#     "Package": "Continuous",
#     "Company": "Nominal"
# }

# for column in types:
#     print(column, ":", types[column])
# print("Mean Package:")
# print(df["Package (LPA)"].mean())
# print()
# print("Median Package:")
# print(df["Package (LPA)"].median())
# print()
# print("Mode Company:")
# print(df["Company"].mode())
# print()
# print("Variance:")
# print(df["Package (LPA)"].var())
# print()
# print("Standard Deviation:")
# print(df["Package (LPA)"].std())
# print("80th Percentile of Package (LPA):")
# print(np.percentile(df["Package (LPA)"],80))
# Q1 = df["Package (LPA)"].quantile(0.25)
# Q3 = df["Package (LPA)"].quantile(0.75)
# IQR = Q3 - Q1
# upper_limit = Q3 + 1.5 * IQR
# high_salary = df[df["Package (LPA)"] > upper_limit]
# print("\nUnusually High Salary Packages:")
# print(high_salary[["Student","Company","Package (LPA)"]])

# Exercise-7

# import pandas as pd
# df = pd.read_csv("ticket.csv")
# print(df)
# print()
# print(df.dtypes)
# print()
# print("Column Types:")
# types = {
#     "Booking_ID": "Nominal",
#     "Movie": "Nominal",
#     "Seat_Type": "Nominal",
#     "Ticket_Price": "Continuous",
#     "Number_of_Tickets": "Discrete",
#     "Booking_Day": "Nominal"
# }
# for column in types:
#     print(column, ":", types[column])
# print()
# print("Calculate Mean Ticket Price")
# print(df["Ticket_Price"].mean())
# print()
# print("Calculate Median Ticket Price")
# print(df["Ticket_Price"].median())
# print()
# print("Calculate Mode of Seat Type")
# print(df["Seat_Type"].mode())
# print()
# print("Calculate Variance")
# print(df["Ticket_Price"].var())
# print()

# print("Calculate Standard Deviation of Ticket Price")
# print(df["Ticket_Price"].std())
# print()
# print("Calculate Q1")
# Q1 = df["Ticket_Price"].quantile(0.25)
# print(Q1)
# print()
# print("Calculate Q2")
# Q2 = df["Ticket_Price"].quantile(0.50)
# print(Q2)
# print()
# print("Calculate Q3")
# Q3 = df["Ticket_Price"].quantile(0.75)
# print(Q3)
# print()
# print("Calculate IQR")
# IQR = Q3 - Q1
# print(IQR)
# print()
# print("Detect Premium-Priced Outliers using the IQR Method")
# lower_limit = Q1 - 1.5 * IQR
# upper_limit = Q3 + 1.5 * IQR
# outliers = df[(df["Ticket_Price"] < lower_limit) | (df["Ticket_Price"] > upper_limit)]
# print("Outlier Limits")
# print("Lower Limit:", lower_limit)
# print("Upper Limit:", upper_limit)
# print()
# print("Premium-Priced Outliers:")
# print(outliers)
# print()
# print("Interpretation")
# if len(outliers) > 0:
#     print("Premium-priced ticket outliers are present in the dataset.")
# else:
#     print("No premium-priced ticket outliers are present in the dataset.")



# Exercise-8

# import pandas as pd
# df=pd.read_csv("restaurant_data.csv")
# print(df)
# print("Mean")
# print(df["Delivery_Time (min)"].mean())
# print()
# print("Median")
# print(df["Distance (km)"].median())
# print()
# print("Mode")
# print(df["Restaurant"].mode())
# print()
# print("Dispersion")
# print("Variance")
# print(df["Delivery_Time (min)"].var())
# print()
# print("Standard Deviation")
# print(df["Delivery_Time (min)"].std())
# print()
# print("Range")
# print(df["Delivery_Time (min)"].max()-df["Delivery_Time (min)"].min())
# print()

# Q1=df["Delivery_Time (min)"].quantile(0.25)
# Q3=df["Delivery_Time (min)"].quantile(0.75)
# IQR=Q3-Q1
# print("IQR",IQR)
# Lower_limit=Q1-1.5*IQR
# Upper_limit=Q1-1.5*IQR
# slow_deliveries = df[df["Delivery_Time (min)"] > Upper_limit]
# print(slow_deliveries.head())

# Exercise-9


# import pandas as pd
# import numpy as np
# df=pd.read_csv("hotel.csv")
# print(df)
# print("Mean")
# print(df["Room_Price"].mean())
# print()
# print("Median")
# print(df["Room_Price"].median())
# print()
# print("Mode")
# print(df["Hotel_Type"].mode())
# print()
# print("Variance")
# print(df["Room_Price"].var())
# print()
# print("Standard Deviation")
# print(df["Room_Price"].std())
# print()
# print("Range")
# print(df["Room_Price"].max()-df["Room_Price"].min())
# print()
# print("20th percentile")
# print(np.percentile(df["Room_Price"],22))
# print("50th percentile")
# print(np.percentile(df["Room_Price"],50))
# print("95th percentile")
# print(np.percentile(df["Room_Price"],95))
# print()
# Q1=df["Room_Price"].quantile(0.25)
# Q3=df["Room_Price"].quantile(0.75)
# IQR=Q3-Q1
# print("IQR",IQR)
# Lower_limit=Q1-1.5*IQR
# Upper_limit=Q3+1.5*IQR
# outliers = df[(df["Room_Price"] < Lower_limit) | (df["Room_Price"] > Upper_limit)]
# print(outliers)
# if df["Room_Price"].mean() > df["Room_Price"].median():
#     print("Median should be used because expensive rooms increase the mean.")
# else:
#     print("Mean can be used because prices are evenly distributed.")


# Exercise-10

# import pandas as pd
# df=pd.read_csv("electricity.csv")
# print(df)
# print()
# print("Mean")
# print(df["Units_Consumed"].mean())
# print()
# print("Median")
# print(df["Units_Consumed"].median())
# print()
# print("mode")
# print(df["City"].mode())
# print()
# print("Range")
# print(df["Units_Consumed"].max()-df["Units_Consumed"].min())
# print()
# print("Variance")
# print(df["Units_Consumed"].var())
# print("Standard Deviation")
# print(df["Units_Consumed"].std())
# print()
# Q1=df["Units_Consumed"].quantile(0.25)
# Q3=df["Units_Consumed"].quantile(0.75)
# IQR=Q3-Q1
# print("IQR",IQR)
# Lower_limit=Q1-1.5*IQR
# Upper_limit=Q3+1.5*IQR
# print("Lower Limit",Lower_limit)
# print("Upper limit",Upper_limit)
# abnormal_usage = df[(df["Units_Consumed"] < Lower_limit) | (df["Units_Consumed"] > Upper_limit)]
# print("Abnormal-Usage",abnormal_usage)
# print("Seasonal Variation Analysis")
# mean_usage = df["Units_Consumed"].mean()
# median_usage = df["Units_Consumed"].median()
# std_usage = df["Units_Consumed"].std()
# print("Mean Usage:", mean_usage)
# print("Median Usage:", median_usage)
# print("Standard Deviation:", std_usage)
# city_average = df.groupby("City")["Units_Consumed"].mean()
# print("Average Consumption by City:")
# print(city_average)


# Exercise-11

# import pandas as pd
# import numpy as np
# df=pd.read_csv("AirportTraffic.csv")
# print(df.head(3))
# print()
# print("Mean")
# print(df["Delay_Minutes"].mean())
# print("Median")
# print(df["Delay_Minutes"].median())
# print()
# print("Mode")
# print(df["Airline"].mode())
# print()
# print("Range")
# print(df["Delay_Minutes"].max()-df["Delay_Minutes"].min())
# print("Variance")
# print(df["Delay_Minutes"].var())
# print()
# print("Standard Deviation")
# print(df["Delay_Minutes"].std())
# Q1= df["Delay_Minutes"].quantile(0.25)
# print("Q1: ",Q1)
# Q2=df["Delay_Minutes"].quantile(0.75)
# print("Q2: ",Q2)
# Q3=df["Delay_Minutes"].quantile(0.95)
# print("Q3: ",Q3)
# print()
# print("IQR")
# IQR=Q3-Q1
# print("IQR",IQR)
# print()
# print("95th percentile")
# print(np.percentile(df["Delay_Minutes"],95))
# IQR = Q3 - Q1
# Lower_limit = Q1 - 1.5 * IQR
# Upper_limit = Q3 + 1.5 * IQR
# print()
# print("IQR:", IQR)
# print("Lower Limit:", Lower_limit)
# print("Upper Limit:", Upper_limit)
# extreme_delays = df[ df["Delay_Minutes"] > Upper_limit]
# print()
# print("Extremely Delayed Flights:")
# print(extreme_delays)


# Exercise-12

# import pandas as pd
# df=pd.read_csv("Cryptocurrency.csv")
# print(df.head(2))
# print()
# print("Mean")
# print(df["Daily_Return (%)"].mean())
# print()
# print("Median")
# print(df["Market_Cap"].median())
# print()
# print("mode")
# print(df["Category"].mode())
# print()
# print("Variance")
# print(df["Daily_Return (%)"].var())
# print()
# print("standard Deviation")
# print(df["Daily_Return (%)"].std())
# print()
# Q1=df["Daily_Return (%)"].quantile(0.25)
# print("Q1",Q1)
# Q3=df["Daily_Return (%)"].quantile(0.95)
# print("Q3",Q3)
# print()
# IQR=Q3-Q1
# print("IQR",IQR)
# print()
# Lower_limit = Q1 - 1.5 * IQR
# Upper_limit = Q3 + 1.5 * IQR
# outliers=df[(df["Daily_Return (%)"]<Lower_limit)|(df["Daily_Return (%)"]>Upper_limit)]
# print(outliers)
# # Volatility analysis means studying how much a value changes over time. In the context of cryptocurrencies, it measures how much the daily returns fluctuate
# print("volatile Analysis")
# std = df["Daily_Return (%)"].std()
# print("Standard Deviation:", std)
# if std > 10:
#     print("Returns are highly volatile because the standard deviation is high.")
# else:
#     print("Returns are relatively stable because the standard deviation is low.")


# Exercise-13


# import pandas as pd
# df=pd.read_csv("Wildlife_Data.csv")
# print(df.head(3))
# print()
# print("DataTypes",df.dtypes)
# print()
# print("Mean")
# print(df["Weight (kg)"].mean())
# print()
# print("median")
# print(df["Weight (kg)"].median())
# print()
# print("Mode")
# print(df["Species"].mode())
# print()
# print("Range")
# print(df["Weight (kg)"].max()-df["Weight (kg)"].min())
# print()
# print("Variance")
# print(df["Weight (kg)"].var())
# print()
# print("Standard Deviation")
# print(df["Weight (kg)"].std())
# print()
# print("Quartiles\n")
# Q1=df["Weight (kg)"].quantile(0.25)
# print("Q1",Q1)
# Q2=df["Weight (kg)"].quantile(0.75)
# print("Q2",Q2)
# Q3=df["Weight (kg)"].quantile(0.95)
# print("Q3",Q3)
# print()
# print("IQR")
# IQR=Q3-Q1
# print(IQR)
# print()
# Lower_limit = Q1 - 1.5 * IQR
# Upper_limit = Q3 + 1.5 * IQR
# print(Lower_limit)
# print(Upper_limit)
# heavy_animals = df[df["Weight (kg)"] > Upper_limit]
# print("Unusually Heavy Animals:")
# print(heavy_animals)



# Exercise-14


# import pandas as pd
# import numpy as np
# df=pd.read_csv("Influencers.csv")
# print(df.head(5))
# print()
# print("Mean")
# print(df["Followers"])
# print()
# print(df["Engagement_Rate"].median())
# print()
# print("Mode")
# print(df["Platform"].mode())
# print()
# print("standard deviation")
# print(df["Engagement_Rate"].std())
# print()
# print("Variance")
# print(df["Engagement_Rate"].var())
# print()
# top_10 = np.percentile(df["Followers"], 90)
# print("90th Percentile (Top 10% Threshold)")
# print(top_10)
# top_influencers = df[df["Followers"] >= top_10]
# print("Top 10% Influencers:")
# print(top_influencers.head(10))
# print("Quartiles\n")
# Q1=df["Followers"].quantile(0.25)
# print("Q1",Q1)
# Q2=df["Followers"].quantile(0.75)
# print("Q2",Q2)
# Q3=df["Followers"].quantile(0.95)
# print("Q3",Q3)
# print()
# print("IQR")
# IQR=Q3-Q1
# print(IQR)
# print()
# Lower_limit = Q1 - 1.5 * IQR
# Upper_limit = Q3 + 1.5 * IQR
# print("Lower_limit",Lower_limit)
# print("Upper_limit",Upper_limit)
# outliers=df[
#     (df["Followers"]<Lower_limit)|
#     (df["Followers"]>Upper_limit)
# ]
# print("Followers Outliers",outliers)
# mean = df["Followers"].mean()
# median = df["Followers"].median()
# print()
# print("Mean:", mean)
# print("Median:", median)
# if mean > median:
#     print("Data is right-skewed. Some influencers have very high followers.")
# elif mean < median:
#     print("Data is left-skewed. Some influencers have very low followers.")
# else:
#     print("Data is approximately normally distributed.")



# exercise-15

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("mars_recover.csv")
print(df.head(1))
print()
print("data types",df.dtypes)
print()
print("mean")
print(df["Temperature"].mean())
print()
print("mode")
print(df["Terrain_Type"].mode())
print()
print("Median")
print(df["Temperature"])
print()
print("Range")
print(df["Temperature"].max()-df["Temperature"].min())
print()
print("Variance")
print(df["Temperature"].var())
print()
print("Standard Deviation")
print(df["Temperature"].std())
print()
Q1=df["Temperature"].quantile(0.25)
print("Q1",Q1)
Q2=df["Temperature"].quantile(0.55)
print("Q2",Q2)
Q3=df["Temperature"].quantile(0.75)
print("Q3",Q3)
print()
IQR=Q3-Q1
print(IQR)
print()
Lower_Limit=Q1-1.5*IQR
print("Lower Limit",Lower_Limit)
Upper_Limit=Q3+1.5*IQR
print("Upper Limit",Upper_Limit)
print()


outliers=df[
    (df["Temperature"]>Lower_Limit) |
    (df["Temperature"]<Upper_Limit)
]
print(outliers)
print()
print("10th percentile")
print(np.percentile(df["Temperature"],10))
print()
print("90th percentile")
print(np.percentile(df["Temperature"],90))
print()
plt.boxplot(df["Temperature"])
plt.title("Temperature Box Plot")
plt.ylabel("Temperature")
plt.show()